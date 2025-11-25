# Generated from ReqSpecL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,72,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,0,1,0,1,1,1,1,3,1,26,8,1,
        1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,5,3,36,8,3,10,3,12,3,39,9,3,1,3,
        1,3,1,4,1,4,1,4,1,4,5,4,47,8,4,10,4,12,4,50,9,4,1,4,1,4,4,4,54,8,
        4,11,4,12,4,55,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,
        7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,0,68,0,17,1,0,0,0,2,25,1,0,
        0,0,4,27,1,0,0,0,6,31,1,0,0,0,8,42,1,0,0,0,10,59,1,0,0,0,12,63,1,
        0,0,0,14,67,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,19,1,0,0,0,19,
        17,1,0,0,0,19,20,1,0,0,0,20,21,1,0,0,0,21,22,5,0,0,1,22,1,1,0,0,
        0,23,26,3,4,2,0,24,26,3,6,3,0,25,23,1,0,0,0,25,24,1,0,0,0,26,3,1,
        0,0,0,27,28,5,4,0,0,28,29,5,10,0,0,29,30,5,1,0,0,30,5,1,0,0,0,31,
        32,5,5,0,0,32,33,5,10,0,0,33,37,5,2,0,0,34,36,3,8,4,0,35,34,1,0,
        0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,37,
        1,0,0,0,40,41,5,3,0,0,41,7,1,0,0,0,42,43,5,6,0,0,43,44,5,11,0,0,
        44,48,5,2,0,0,45,47,3,10,5,0,46,45,1,0,0,0,47,50,1,0,0,0,48,46,1,
        0,0,0,48,49,1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,0,51,53,3,12,6,0,52,
        54,3,14,7,0,53,52,1,0,0,0,54,55,1,0,0,0,55,53,1,0,0,0,55,56,1,0,
        0,0,56,57,1,0,0,0,57,58,5,3,0,0,58,9,1,0,0,0,59,60,5,7,0,0,60,61,
        5,11,0,0,61,62,5,1,0,0,62,11,1,0,0,0,63,64,5,8,0,0,64,65,5,11,0,
        0,65,66,5,1,0,0,66,13,1,0,0,0,67,68,5,9,0,0,68,69,5,11,0,0,69,70,
        5,1,0,0,70,15,1,0,0,0,5,19,25,37,48,55
    ]

class ReqSpecLParser ( Parser ):

    grammarFileName = "ReqSpecL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'{'", "'}'", "'def_actor'", "'def_feature'", 
                     "'scenario'", "'given'", "'when'", "'then'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "KW_ACTOR", "KW_FEATURE", "KW_SCENARIO", "KW_GIVEN", 
                      "KW_WHEN", "KW_THEN", "ID", "STRING", "WS", "SL_COMMENT" ]

    RULE_program = 0
    RULE_definition = 1
    RULE_actor_def = 2
    RULE_feature_def = 3
    RULE_scenario_def = 4
    RULE_given_clause = 5
    RULE_when_clause = 6
    RULE_then_clause = 7

    ruleNames =  [ "program", "definition", "actor_def", "feature_def", 
                   "scenario_def", "given_clause", "when_clause", "then_clause" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    KW_ACTOR=4
    KW_FEATURE=5
    KW_SCENARIO=6
    KW_GIVEN=7
    KW_WHEN=8
    KW_THEN=9
    ID=10
    STRING=11
    WS=12
    SL_COMMENT=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ReqSpecLParser.EOF, 0)

        def definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ReqSpecLParser.DefinitionContext)
            else:
                return self.getTypedRuleContext(ReqSpecLParser.DefinitionContext,i)


        def getRuleIndex(self):
            return ReqSpecLParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ReqSpecLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.definition()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4 or _la==5):
                    break

            self.state = 21
            self.match(ReqSpecLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def actor_def(self):
            return self.getTypedRuleContext(ReqSpecLParser.Actor_defContext,0)


        def feature_def(self):
            return self.getTypedRuleContext(ReqSpecLParser.Feature_defContext,0)


        def getRuleIndex(self):
            return ReqSpecLParser.RULE_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinition" ):
                listener.enterDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinition" ):
                listener.exitDefinition(self)




    def definition(self):

        localctx = ReqSpecLParser.DefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_definition)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.actor_def()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.feature_def()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Actor_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ACTOR(self):
            return self.getToken(ReqSpecLParser.KW_ACTOR, 0)

        def ID(self):
            return self.getToken(ReqSpecLParser.ID, 0)

        def getRuleIndex(self):
            return ReqSpecLParser.RULE_actor_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActor_def" ):
                listener.enterActor_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActor_def" ):
                listener.exitActor_def(self)




    def actor_def(self):

        localctx = ReqSpecLParser.Actor_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_actor_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(ReqSpecLParser.KW_ACTOR)
            self.state = 28
            self.match(ReqSpecLParser.ID)
            self.state = 29
            self.match(ReqSpecLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Feature_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FEATURE(self):
            return self.getToken(ReqSpecLParser.KW_FEATURE, 0)

        def ID(self):
            return self.getToken(ReqSpecLParser.ID, 0)

        def scenario_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ReqSpecLParser.Scenario_defContext)
            else:
                return self.getTypedRuleContext(ReqSpecLParser.Scenario_defContext,i)


        def getRuleIndex(self):
            return ReqSpecLParser.RULE_feature_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeature_def" ):
                listener.enterFeature_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeature_def" ):
                listener.exitFeature_def(self)




    def feature_def(self):

        localctx = ReqSpecLParser.Feature_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_feature_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(ReqSpecLParser.KW_FEATURE)
            self.state = 32
            self.match(ReqSpecLParser.ID)
            self.state = 33
            self.match(ReqSpecLParser.T__1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 34
                self.scenario_def()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(ReqSpecLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scenario_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_SCENARIO(self):
            return self.getToken(ReqSpecLParser.KW_SCENARIO, 0)

        def STRING(self):
            return self.getToken(ReqSpecLParser.STRING, 0)

        def when_clause(self):
            return self.getTypedRuleContext(ReqSpecLParser.When_clauseContext,0)


        def given_clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ReqSpecLParser.Given_clauseContext)
            else:
                return self.getTypedRuleContext(ReqSpecLParser.Given_clauseContext,i)


        def then_clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ReqSpecLParser.Then_clauseContext)
            else:
                return self.getTypedRuleContext(ReqSpecLParser.Then_clauseContext,i)


        def getRuleIndex(self):
            return ReqSpecLParser.RULE_scenario_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScenario_def" ):
                listener.enterScenario_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScenario_def" ):
                listener.exitScenario_def(self)




    def scenario_def(self):

        localctx = ReqSpecLParser.Scenario_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_scenario_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(ReqSpecLParser.KW_SCENARIO)
            self.state = 43
            self.match(ReqSpecLParser.STRING)
            self.state = 44
            self.match(ReqSpecLParser.T__1)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 45
                self.given_clause()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self.when_clause()
            self.state = 53 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 52
                self.then_clause()
                self.state = 55 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
                    break

            self.state = 57
            self.match(ReqSpecLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Given_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_GIVEN(self):
            return self.getToken(ReqSpecLParser.KW_GIVEN, 0)

        def STRING(self):
            return self.getToken(ReqSpecLParser.STRING, 0)

        def getRuleIndex(self):
            return ReqSpecLParser.RULE_given_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGiven_clause" ):
                listener.enterGiven_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGiven_clause" ):
                listener.exitGiven_clause(self)




    def given_clause(self):

        localctx = ReqSpecLParser.Given_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_given_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(ReqSpecLParser.KW_GIVEN)
            self.state = 60
            self.match(ReqSpecLParser.STRING)
            self.state = 61
            self.match(ReqSpecLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class When_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_WHEN(self):
            return self.getToken(ReqSpecLParser.KW_WHEN, 0)

        def STRING(self):
            return self.getToken(ReqSpecLParser.STRING, 0)

        def getRuleIndex(self):
            return ReqSpecLParser.RULE_when_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhen_clause" ):
                listener.enterWhen_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhen_clause" ):
                listener.exitWhen_clause(self)




    def when_clause(self):

        localctx = ReqSpecLParser.When_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_when_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(ReqSpecLParser.KW_WHEN)
            self.state = 64
            self.match(ReqSpecLParser.STRING)
            self.state = 65
            self.match(ReqSpecLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Then_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_THEN(self):
            return self.getToken(ReqSpecLParser.KW_THEN, 0)

        def STRING(self):
            return self.getToken(ReqSpecLParser.STRING, 0)

        def getRuleIndex(self):
            return ReqSpecLParser.RULE_then_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThen_clause" ):
                listener.enterThen_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThen_clause" ):
                listener.exitThen_clause(self)




    def then_clause(self):

        localctx = ReqSpecLParser.Then_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_then_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(ReqSpecLParser.KW_THEN)
            self.state = 68
            self.match(ReqSpecLParser.STRING)
            self.state = 69
            self.match(ReqSpecLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





