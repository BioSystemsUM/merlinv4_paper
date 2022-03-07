from unittest import TestCase

from Scripts.assessment import ModelAssessor
from Scripts.core import read_sbml_into_cobra_model
from Scripts.utils import ReconstructionTool


class TestAssessment(TestCase):

    def test_merlin_reaction_ids_conversion(self):
        model2_model_seed = read_sbml_into_cobra_model(file_path="../Models/Merlin/Bpertussis.xml",
                                                       database_version="kegg",
                                                       reconstruction_tool=ReconstructionTool.MERLIN.value)

        reactions = ModelAssessor.convert_reactions({"merlin": model2_model_seed})


