# Generated from ReqSpecL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ReqSpecLParser import ReqSpecLParser
else:
    from ReqSpecLParser import ReqSpecLParser

# This class defines a complete listener for a parse tree produced by ReqSpecLParser.
class ReqSpecLListener(ParseTreeListener):

    # Enter a parse tree produced by ReqSpecLParser#program.
    def enterProgram(self, ctx:ReqSpecLParser.ProgramContext):
        pass

    # Exit a parse tree produced by ReqSpecLParser#program.
    def exitProgram(self, ctx:ReqSpecLParser.ProgramContext):
        pass


    # Enter a parse tree produced by ReqSpecLParser#definition.
    def enterDefinition(self, ctx:ReqSpecLParser.DefinitionContext):
        pass

    # Exit a parse tree produced by ReqSpecLParser#definition.
    def exitDefinition(self, ctx:ReqSpecLParser.DefinitionContext):
        pass


    # Enter a parse tree produced by ReqSpecLParser#var_def.
    def enterVar_def(self, ctx:ReqSpecLParser.Var_defContext):
        pass

    # Exit a parse tree produced by ReqSpecLParser#var_def.
    def exitVar_def(self, ctx:ReqSpecLParser.Var_defContext):
        pass


    # Enter a parse tree produced by ReqSpecLParser#endpoint_def.
    def enterEndpoint_def(self, ctx:ReqSpecLParser.Endpoint_defContext):
        pass

    # Exit a parse tree produced by ReqSpecLParser#endpoint_def.
    def exitEndpoint_def(self, ctx:ReqSpecLParser.Endpoint_defContext):
        pass


    # Enter a parse tree produced by ReqSpecLParser#method.
    def enterMethod(self, ctx:ReqSpecLParser.MethodContext):
        pass

    # Exit a parse tree produced by ReqSpecLParser#method.
    def exitMethod(self, ctx:ReqSpecLParser.MethodContext):
        pass


    # Enter a parse tree produced by ReqSpecLParser#actor_def.
    def enterActor_def(self, ctx:ReqSpecLParser.Actor_defContext):
        pass

    # Exit a parse tree produced by ReqSpecLParser#actor_def.
    def exitActor_def(self, ctx:ReqSpecLParser.Actor_defContext):
        pass


    # Enter a parse tree produced by ReqSpecLParser#feature_def.
    def enterFeature_def(self, ctx:ReqSpecLParser.Feature_defContext):
        pass

    # Exit a parse tree produced by ReqSpecLParser#feature_def.
    def exitFeature_def(self, ctx:ReqSpecLParser.Feature_defContext):
        pass


    # Enter a parse tree produced by ReqSpecLParser#scenario_def.
    def enterScenario_def(self, ctx:ReqSpecLParser.Scenario_defContext):
        pass

    # Exit a parse tree produced by ReqSpecLParser#scenario_def.
    def exitScenario_def(self, ctx:ReqSpecLParser.Scenario_defContext):
        pass


    # Enter a parse tree produced by ReqSpecLParser#given_clause.
    def enterGiven_clause(self, ctx:ReqSpecLParser.Given_clauseContext):
        pass

    # Exit a parse tree produced by ReqSpecLParser#given_clause.
    def exitGiven_clause(self, ctx:ReqSpecLParser.Given_clauseContext):
        pass


    # Enter a parse tree produced by ReqSpecLParser#when_clause.
    def enterWhen_clause(self, ctx:ReqSpecLParser.When_clauseContext):
        pass

    # Exit a parse tree produced by ReqSpecLParser#when_clause.
    def exitWhen_clause(self, ctx:ReqSpecLParser.When_clauseContext):
        pass


    # Enter a parse tree produced by ReqSpecLParser#then_clause.
    def enterThen_clause(self, ctx:ReqSpecLParser.Then_clauseContext):
        pass

    # Exit a parse tree produced by ReqSpecLParser#then_clause.
    def exitThen_clause(self, ctx:ReqSpecLParser.Then_clauseContext):
        pass


    # Enter a parse tree produced by ReqSpecLParser#error_clause.
    def enterError_clause(self, ctx:ReqSpecLParser.Error_clauseContext):
        pass

    # Exit a parse tree produced by ReqSpecLParser#error_clause.
    def exitError_clause(self, ctx:ReqSpecLParser.Error_clauseContext):
        pass



del ReqSpecLParser