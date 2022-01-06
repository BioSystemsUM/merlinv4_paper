import pandas

from ModelsComparisonMetrics import ModelsComparisonMetrics
from utils import Utils, Type
from cobra.io.sbml import read_sbml_model

def getBordetellaPertussis_models() -> dict:
    BordetellaPertussis_rast_model = read_sbml_model("./models/BordetellaPertussis-rast-model.xml")
    BordetellaPertussis_blast_model = read_sbml_model("./models/BordetellaPertussis-blast-model.xml")
    BordetellaPertussis_diamond_fast_model = read_sbml_model("./models/BordetellaPertussis-diamond-fast-model.xml")
    BordetellaPertussis_diamond_sensitive_model = read_sbml_model("./models/BordetellaPertussis-diamond-sensitive-model.xml")
    BordetellaPertussis_diamond_very_sensitive_model = read_sbml_model("./models/BordetellaPertussis-diamond-very-sensitive-model.xml")
    BordetellaPertussis_diamond_ultra_sensitive_model = read_sbml_model("./models/BordetellaPertussis-diamond-ultra-sensitive-model.xml")

    BordetellaPertussis_models = {"rast model": BordetellaPertussis_rast_model,
                                  "blast model": BordetellaPertussis_blast_model,
                                  "diamond fast model": BordetellaPertussis_diamond_fast_model,
                                  "diamond sensitive model": BordetellaPertussis_diamond_sensitive_model,
                                  "diamond very-sensitive model": BordetellaPertussis_diamond_very_sensitive_model,
                                  "diamond ultra-sensitive model": BordetellaPertussis_diamond_ultra_sensitive_model
                                  }

    return BordetellaPertussis_models

def getKomagataeibacterSucrofermentans_models() -> dict:
    KomagataeibacterSucrofermentans_rast_model = read_sbml_model("./models/KomagataeibacterSucrofermentans-rast-model.xml")
    KomagataeibacterSucrofermentans_blast_model = read_sbml_model("./models/KomagataeibacterSucrofermentans-blast-model.xml")
    KomagataeibacterSucrofermentans_diamond_fast_model = read_sbml_model("./models/KomagataeibacterSucrofermentans-diamond-fast-model.xml")
    KomagataeibacterSucrofermentans_diamond_sensitive_model = read_sbml_model("./models/KomagataeibacterSucrofermentans-diamond-sensitive-model.xml")
    KomagataeibacterSucrofermentans_diamond_very_sensitive_model = read_sbml_model("./models/KomagataeibacterSucrofermentans-diamond-very-sensitive-model.xml")
    KomagataeibacterSucrofermentans_diamond_ultra_sensitive_model = read_sbml_model("./models/KomagataeibacterSucrofermentans-diamond-ultra-sensitive-model.xml")

    KomagataeibacterSucrofermentans_models = {"rast model": KomagataeibacterSucrofermentans_rast_model,
                                              "blast model": KomagataeibacterSucrofermentans_blast_model,
                                              "diamond fast model": KomagataeibacterSucrofermentans_diamond_fast_model,
                                              "diamond sensitive model": KomagataeibacterSucrofermentans_diamond_sensitive_model,
                                              "diamond very-sensitive model": KomagataeibacterSucrofermentans_diamond_very_sensitive_model,
                                              "diamond ultra-sensitive model": KomagataeibacterSucrofermentans_diamond_ultra_sensitive_model
                                              }

    return KomagataeibacterSucrofermentans_models

def getLactobacillusPlantarum_models() -> dict:
    LactobacillusPlantarum_rast_model = read_sbml_model("./models/LactobacillusPlantarum-rast-model.xml")
    LactobacillusPlantarum_blast_model = read_sbml_model("./models/LactobacillusPlantarum-blast-model.xml")
    LactobacillusPlantarum_diamond_fast_model = read_sbml_model("./models/LactobacillusPlantarum-diamond-fast-model.xml")
    LactobacillusPlantarum_diamond_sensitive_model = read_sbml_model("./models/LactobacillusPlantarum-diamond-sensitive-model.xml")
    LactobacillusPlantarum_diamond_very_sensitive_model = read_sbml_model("./models/LactobacillusPlantarum-diamond-very-sensitive-model.xml")
    LactobacillusPlantarum_diamond_ultra_sensitive_model = read_sbml_model("./models/LactobacillusPlantarum-diamond-ultra-sensitive-model.xml")

    LactobacillusPlantarum_models = {"rast model": LactobacillusPlantarum_rast_model,
                                     "blast model": LactobacillusPlantarum_blast_model,
                                     "diamond fast model": LactobacillusPlantarum_diamond_fast_model,
                                     "diamond sensitive model": LactobacillusPlantarum_diamond_sensitive_model,
                                     "diamond very-sensitive model": LactobacillusPlantarum_diamond_very_sensitive_model,
                                     "diamond ultra-sensitive model": LactobacillusPlantarum_diamond_ultra_sensitive_model
                                     }

    return LactobacillusPlantarum_models

def getPseudomonasPutida_models() -> dict:
    PseudomonasPutida_rast_model = read_sbml_model("./models/PseudomonasPutida-rast-model.xml")
    PseudomonasPutida_blast_model = read_sbml_model("./models/PseudomonasPutida-blast-model.xml")
    PseudomonasPutida_diamond_fast_model = read_sbml_model("./models/PseudomonasPutida-diamond-fast-model.xml")
    PseudomonasPutida_diamond_sensitive_model = read_sbml_model("./models/PseudomonasPutida-diamond-sensitive-model.xml")
    PseudomonasPutida_diamond_very_sensitive_model = read_sbml_model("./models/PseudomonasPutida-diamond-very-sensitive-model.xml")
    PseudomonasPutida_diamond_ultra_sensitive_model = read_sbml_model("./models/PseudomonasPutida-diamond-ultra-sensitive-model.xml")

    PseudomonasPutida_models = {"rast model": PseudomonasPutida_rast_model,
                                "blast model": PseudomonasPutida_blast_model,
                                "diamond fast model": PseudomonasPutida_diamond_fast_model,
                                "diamond sensitive model": PseudomonasPutida_diamond_sensitive_model,
                                "diamond very-sensitive model": PseudomonasPutida_diamond_very_sensitive_model,
                                "diamond ultra-sensitive model": PseudomonasPutida_diamond_ultra_sensitive_model
                                }

    return PseudomonasPutida_models

def resultsGeneration_BordetellaPertussis () -> None:
    BordetellaPertussis_models = getBordetellaPertussis_models()
    modelsComparisonMetrics = ModelsComparisonMetrics(BordetellaPertussis_models)
    modelsComparisonMetrics.draw_venn_diagram(Type.GENES, "./results/BordetellaPertussis-genes-venn-diagram.jpeg")
    modelsComparisonMetrics.draw_venn_diagram(Type.METABOLITES, "./results/BordetellaPertussis-metabolites-venn-diagram.jpeg")
    modelsComparisonMetrics.draw_venn_diagram(Type.REACTIONS, "./results/BordetellaPertussis-reactions-venn-diagram.jpeg")

    modelsComparisonMetrics.write_reaction_genes_metabolites_into_csv(organism="Bordetella Pertussis",
                                                                      output_path_non_curated_models="./results/BordetellaPertussis-stats.csv",
                                                                      output_path_curated_models="")

def resultsGeneration_KomagataeibacterSucrofermentans () -> None:
    KomagataeibacterSucrofermentans_models = getKomagataeibacterSucrofermentans_models()
    modelsComparisonMetrics = ModelsComparisonMetrics(KomagataeibacterSucrofermentans_models)
    modelsComparisonMetrics.draw_venn_diagram(Type.GENES, "./results/KomagataeibacterSucrofermentans-genes-venn-diagram.jpeg")
    modelsComparisonMetrics.draw_venn_diagram(Type.METABOLITES, "./results/KomagataeibacterSucrofermentans-metabolites-venn-diagram.jpeg")
    modelsComparisonMetrics.draw_venn_diagram(Type.REACTIONS, "./results/KomagataeibacterSucrofermentans-reactions-venn-diagram.jpeg")

    modelsComparisonMetrics.write_reaction_genes_metabolites_into_csv(organism="Komagataeibacter Sucrofermentans",
                                                                      output_path_non_curated_models="./results/KomagataeibacterSucrofermentans-stats.csv",
                                                                      output_path_curated_models="")

def resultsGeneration_LactobacillusPlantarum () -> None:
    LactobacillusPlantarum_models = getLactobacillusPlantarum_models()
    modelsComparisonMetrics = ModelsComparisonMetrics(LactobacillusPlantarum_models)
    modelsComparisonMetrics.draw_venn_diagram(Type.GENES, "./results/LactobacillusPlantarum-genes-venn-diagram.jpeg")
    modelsComparisonMetrics.draw_venn_diagram(Type.METABOLITES, "./results/LactobacillusPlantarum-metabolites-venn-diagram.jpeg")
    modelsComparisonMetrics.draw_venn_diagram(Type.REACTIONS, "./results/LactobacillusPlantarum-reactions-venn-diagram.jpeg")

    modelsComparisonMetrics.write_reaction_genes_metabolites_into_csv(organism="Lactobacillus Plantarum",
                                                                      output_path_non_curated_models="./results/LactobacillusPlantarum-stats.csv",
                                                                      output_path_curated_models="")

def resultsGeneration_PseudomonasPutida () -> None:
    PseudomonasPutida_models = getPseudomonasPutida_models()
    modelsComparisonMetrics = ModelsComparisonMetrics(PseudomonasPutida_models)
    modelsComparisonMetrics.draw_venn_diagram(Type.GENES, "./results/PseudomonasPutida-genes-venn-diagram.jpeg")
    modelsComparisonMetrics.draw_venn_diagram(Type.METABOLITES, "./results/PseudomonasPutida-metabolites-venn-diagram.jpeg")
    modelsComparisonMetrics.draw_venn_diagram(Type.REACTIONS, "./results/PseudomonasPutida-reactions-venn-diagram.jpeg")

    modelsComparisonMetrics.write_reaction_genes_metabolites_into_csv(organism="Pseudomonas Putida",
                                                                      output_path_non_curated_models="./results/PseudomonasPutida-stats.csv",
                                                                      output_path_curated_models="")

def resultsGeneration_executionTime () -> None:
    execution_time_values = pandas.read_excel("./results/execution-time-values.xlsx")
    ModelsComparisonMetrics.draw_barplot(execution_time_values, "./results/execution-time-values-barplot.jpeg")

if __name__=="__main__":

    print("Generating results related with the execution time")
    resultsGeneration_executionTime()

    print("Generating results for Bordetella Pertussis")
    resultsGeneration_BordetellaPertussis()

    print("Generating results for Komagataeibacter Sucrofermentans")
    resultsGeneration_KomagataeibacterSucrofermentans()

    print("Generating results for Lactobacillus Plantarum")
    resultsGeneration_LactobacillusPlantarum()

    print("Generating results for Pseudomonas Putida")
    resultsGeneration_PseudomonasPutida()
