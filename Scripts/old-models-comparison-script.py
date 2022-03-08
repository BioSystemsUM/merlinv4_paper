import matplotlib
import seaborn

from xrefs_converters import ReactionsConverter
from ModelsComparisonMetrics import ModelsComparisonMetrics
from core import read_sbml_into_cobra_model
from utils import Utils, Type, ReconstructionTool
from cobra.io.sbml import read_sbml_model
import pandas
from Bio import SeqIO, GenBank


def getModels(organism) -> dict:
    # comparison models
    aureme_model = read_sbml_into_cobra_model(file_path="../Models/AuReMe/" + str(organism) + ".xml",
                                              database_version="bigg",
                                              reconstruction_tool=ReconstructionTool.AUREME)

    autokeggrec_model = read_sbml_into_cobra_model(file_path="../Models/AutoKEGGRec/" + str(organism) + ".xml",
                                                   database_version="kegg",
                                                   reconstruction_tool=ReconstructionTool.AUTOKEGGREC)

    carveme_model = read_sbml_into_cobra_model(file_path="../Models/CarveMe/" + str(organism) + ".xml",
                                               database_version="bigg",
                                               reconstruction_tool=ReconstructionTool.CARVEME)

    modelseed_model = read_sbml_into_cobra_model(file_path="../Models/ModelSEED/" + str(organism) + ".xml",
                                                 database_version="modelseed",
                                                 reconstruction_tool=ReconstructionTool.MODELSEED)

    pathwaytools_model = read_sbml_into_cobra_model(file_path="../Models/PathwayTools/" + str(organism) + ".xml",
                                                    database_version="metacyc",
                                                    reconstruction_tool=ReconstructionTool.PATHWAYTOOLS)

    raven_model = read_sbml_into_cobra_model(file_path="../Models/RAVEN/" + str(organism) + ".xml",
                                             database_version="kegg",
                                             reconstruction_tool=ReconstructionTool.RAVEN)

    merlin_model = read_sbml_into_cobra_model(file_path="../Models/Merlin/" + str(organism) + ".xml",
                                              database_version="kegg",
                                              reconstruction_tool=ReconstructionTool.MERLIN)

    merlin_bit_model = read_sbml_into_cobra_model(file_path="../Models/Merlin-BIT/" + str(organism) + ".xml",
                                                  database_version="bigg",
                                                  reconstruction_tool=ReconstructionTool.MERLIN)

    # reference model
    reference_model = read_sbml_into_cobra_model(file_path="../Models/Manually_curated/" + str(organism) + ".xml",
                                                 database_version="bigg",
                                                 reconstruction_tool=None)

    models = {"aureme model": aureme_model,
              "autokeggrec model": autokeggrec_model,
              "carveme model": carveme_model,
              "modelseed model": modelseed_model,
              "pathwaytools model": pathwaytools_model,
              "raven model": raven_model,
              "merlin model": merlin_model,
              "merlin bit model": merlin_bit_model,
              "reference model": reference_model
              }

    return models


def getReactionSets(models) -> dict:
    reaction_sets = {}

    for model_name in models.keys():

        reaction_set = []
        model = models[model_name]

        all_reactions = model.model.reactions
        reactions_to_convert = []

        transport_reactions = {}

        for group in model.model.groups:
            reactions_list = []
            if "transport" in str(group.name).lower() or "drain" in str(group.name).lower():
                for member in group.members:
                    reactions_list.append(member.id)
                transport_reactions[str(group.name)] = reactions_list

        for reaction in all_reactions:
            reaction_id = reaction.id

            add = True

            # exclude exchange reactions from the comparison
            if len(model.model.exchanges) > 0 and add:
                if reaction in model.model.exchanges:
                    add = False

            if "drain" in str(reaction.name).lower() and add:
                add = False

            if "exchange" in str(reaction.name).lower() and add:
                add = False

            if str(reaction_id).upper().startswith("EX_") and add:
                add = False

            # exclude demand reactions from the comparison
            if len(model.model.demands) > 0 and add:
                if reaction in model.model.demands:
                    add = False

            # exclude transport reactions from the comparison
            if len(model.model.sinks) > 0 and add:
                if reaction in model.model.sinks:
                    add = False

            # exclude transport reactions from the comparison
            if "transport" in str(reaction.name).lower() and add:
                add = False

            if str(reaction_id).upper().startswith("TRANS-RXN") and add:
                add = False

            if "TRANS-RXN" in str(reaction.name).upper() and add:
                add = False

            if len(transport_reactions) > 0 and add:
                for group in transport_reactions.values():
                    if reaction_id in group:
                        add = False
                        break

            if add:
                reactions_to_convert.append(reaction_id)

        ModelSEED_reactions_converter = ReactionsConverter("xrefs_files/ModelSEED-reactions.csv")
        model.reaction_converter = ModelSEED_reactions_converter
        ModelSEED_report = model.get_reactions_other_version(database="modelseed",
                                                             reactions=reactions_to_convert,
                                                             preprocess_ids=True)
        ModelSEED_convertable_reactions = ModelSEED_report.convertable

        print("Tool: " + str(model.reconstruction_tool))
        print("Total number of reactions: " + str(len(model.model.reactions)))

        print("Reactions converted with ModelSEED: " + str(len(ModelSEED_convertable_reactions.keys())))
        print("Reactions not converted with ModelSEED: " + str(len(ModelSEED_report.non_convertable)))

        for convertable_reaction in ModelSEED_convertable_reactions:
            converted_reactions = ModelSEED_convertable_reactions[convertable_reaction]

            if len(converted_reactions) > 1:
                dic = {}
                for converted_reaction in converted_reactions:
                    dic[converted_reaction] = 0
                    for model in reaction_sets.keys():
                        if converted_reaction in reaction_sets[model]:
                            dic[converted_reaction] = int(dic[converted_reaction]) + 1

                dic = dict(sorted(dic.items(), key=lambda item: item[1]))
                reaction_set.append((str(list(dic.keys())[-1])).upper())
            else:
                for converted_reaction in converted_reactions:
                    if converted_reaction not in reaction_set:
                        reaction_set.append(str(converted_reaction).upper())


        ModelSEED_non_convertable_reactions = ModelSEED_report.non_convertable
        MetaNetX_reactions_converter = ReactionsConverter("xrefs_files/MetaNetX-reactions.csv")
        model.reaction_converter = MetaNetX_reactions_converter
        MetaNetX_report = model.get_reactions_other_version(database="metanetx",
                                                            reactions=ModelSEED_non_convertable_reactions,
                                                            preprocess_ids=False)
        MetaNetX_convertable_reactions = MetaNetX_report.convertable

        print("Reactions converted with MetaNetX: " + str(len(MetaNetX_convertable_reactions.keys())))
        print("Reactions not converted with MetaNetX: " + str(len(MetaNetX_report.non_convertable)))
        print(MetaNetX_report.non_convertable)
        print()

        for convertable_reaction in MetaNetX_convertable_reactions:
            converted_reactions = MetaNetX_convertable_reactions[convertable_reaction]

            if len(converted_reactions) > 1:
                dic = {}
                for converted_reaction in converted_reactions:
                    dic[converted_reaction] = 0
                    for model in reaction_sets.keys():
                        if converted_reaction in reaction_sets[model]:
                            dic[converted_reaction] = int(dic[converted_reaction]) + 1

                dic = dict(sorted(dic.items(), key=lambda item: item[1]))
                reaction_set.append((str(list(dic.keys())[-1])).upper())
            else:
                for converted_reaction in converted_reactions:
                    if converted_reaction not in reaction_set:
                        reaction_set.append(str(converted_reaction).upper())

        reaction_sets[model_name] = set(reaction_set)
    return reaction_sets


def getGeneSets(models) -> dict:
    gene_sets = {}

    for model_name in models.keys():
        gene_set = []
        model = models[model_name]
        for gene in model.model.genes:
            gene_set.append((str(gene.id)).upper())
        gene_sets[model_name] = set(gene_set)
    return gene_sets


def resultsGeneration(organism, genes_dotplot_path, reactions_dotplot_path) -> None:
    models = getModels(organism=organism)
    modelsComparisonMetrics = ModelsComparisonMetrics(models=models)

    gene_sets = getGeneSets(models=models)
    modelsComparisonMetrics.set_gene_sets(gene_sets=gene_sets)

    reaction_sets = getReactionSets(models=models)
    modelsComparisonMetrics.set_reaction_sets(reaction_sets=reaction_sets)

    # Genes

    jaccard_distances_genes = modelsComparisonMetrics.calculate_jaccard_distances(
        reference_model_name="reference model",
        type=Type.GENES)
    ratios_genes = modelsComparisonMetrics.calculate_ratios(
        reference_model_name="reference model",
        type=Type.GENES)

    gene_sets.pop("reference model")
    modelsComparisonMetrics.set_gene_sets(gene_sets=gene_sets)

    modelsComparisonMetrics.draw_dot_plot(jaccard_distances=jaccard_distances_genes,
                                          ratios=ratios_genes,
                                          output_path=genes_dotplot_path)

    # Reactions

    jaccard_distances_reactions = modelsComparisonMetrics.calculate_jaccard_distances(
        reference_model_name="reference model",
        type=Type.REACTIONS)
    ratios_reactions = modelsComparisonMetrics.calculate_ratios(reference_model_name="reference model",
                                                                type=Type.REACTIONS)

    reaction_sets.pop("reference model")
    modelsComparisonMetrics.set_reaction_sets(reaction_sets=reaction_sets)

    modelsComparisonMetrics.draw_dot_plot(jaccard_distances=jaccard_distances_reactions,
                                          ratios=ratios_reactions,
                                          output_path=reactions_dotplot_path)


if __name__ == "__main__":

    print("Generating results for Bordetella pertussis")
    resultsGeneration(organism="Bpertussis",
                      genes_dotplot_path="../results/Bpertussis-genes-dot-plot.jpeg",
                      reactions_dotplot_path="../results/Bpertussis-reactions-dot-plot.jpeg")

    # print("Generating results for Chlorella vulgaris")
    # resultsGeneration(organism="Cvulgaris",
    #                   genes_dotplot_path="results/Cvulgaris-genes-dot-plot.jpeg",
    #                   reactions_dotplot_path="results/Cvulgaris-reactions-dot-plot.jpeg")

    print("Generating results for Lactobacillus plantarum")
    resultsGeneration(organism="Lplantarum",
                      genes_dotplot_path="../results/Lplantarum-genes-dot-plot.jpeg",
                      reactions_dotplot_path="../results/Lplantarum-reactions-dot-plot.jpeg")

    # print("Generating results for Toxoplasma gondii")
    # resultsGeneration(organism="Tgondii ",
    #                   genes_dotplot_path="results/Tgondii-genes-dot-plot.jpeg",
    #                   reactions_dotplot_path="results/Tgondii-reactions-dot-plot.jpeg")
