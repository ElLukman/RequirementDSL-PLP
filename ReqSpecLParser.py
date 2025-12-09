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
        4,1,21,104,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,0,1,0,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,
        1,6,5,6,60,8,6,10,6,12,6,63,9,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,71,8,
        7,10,7,12,7,74,9,7,1,7,1,7,5,7,78,8,7,10,7,12,7,81,9,7,1,7,3,7,84,
        8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,11,1,11,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,
        2,1,0,3,6,1,0,18,19,99,0,25,1,0,0,0,2,35,1,0,0,0,4,37,1,0,0,0,6,
        43,1,0,0,0,8,49,1,0,0,0,10,51,1,0,0,0,12,55,1,0,0,0,14,66,1,0,0,
        0,16,87,1,0,0,0,18,91,1,0,0,0,20,95,1,0,0,0,22,99,1,0,0,0,24,26,
        3,2,1,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,
        28,29,1,0,0,0,29,30,5,0,0,1,30,1,1,0,0,0,31,36,3,10,5,0,32,36,3,
        4,2,0,33,36,3,6,3,0,34,36,3,12,6,0,35,31,1,0,0,0,35,32,1,0,0,0,35,
        33,1,0,0,0,35,34,1,0,0,0,36,3,1,0,0,0,37,38,5,11,0,0,38,39,5,18,
        0,0,39,40,5,1,0,0,40,41,5,19,0,0,41,42,5,2,0,0,42,5,1,0,0,0,43,44,
        5,12,0,0,44,45,5,18,0,0,45,46,3,8,4,0,46,47,5,19,0,0,47,48,5,2,0,
        0,48,7,1,0,0,0,49,50,7,0,0,0,50,9,1,0,0,0,51,52,5,9,0,0,52,53,5,
        18,0,0,53,54,5,2,0,0,54,11,1,0,0,0,55,56,5,10,0,0,56,57,5,18,0,0,
        57,61,5,7,0,0,58,60,3,14,7,0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,
        0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,0,64,65,5,8,0,0,65,
        13,1,0,0,0,66,67,5,13,0,0,67,68,5,19,0,0,68,72,5,7,0,0,69,71,3,16,
        8,0,70,69,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,75,
        1,0,0,0,74,72,1,0,0,0,75,79,3,18,9,0,76,78,3,20,10,0,77,76,1,0,0,
        0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,83,1,0,0,0,81,79,
        1,0,0,0,82,84,3,22,11,0,83,82,1,0,0,0,83,84,1,0,0,0,84,85,1,0,0,
        0,85,86,5,8,0,0,86,15,1,0,0,0,87,88,5,14,0,0,88,89,7,1,0,0,89,90,
        5,2,0,0,90,17,1,0,0,0,91,92,5,15,0,0,92,93,5,19,0,0,93,94,5,2,0,
        0,94,19,1,0,0,0,95,96,5,16,0,0,96,97,5,19,0,0,97,98,5,2,0,0,98,21,
        1,0,0,0,99,100,5,17,0,0,100,101,5,19,0,0,101,102,5,2,0,0,102,23,
        1,0,0,0,6,27,35,61,72,79,83
    ]

class ReqSpecLParser ( Parser ):

    grammarFileName = "ReqSpecL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'GET'", "'POST'", "'PUT'", 
                     "'DELETE'", "'{'", "'}'", "'def_actor'", "'def_feature'", 
                     "'def_context'", "'def_endpoint'", "'scenario'", "'given'", 
                     "'when'", "'then'", "'expect_error'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "KW_ACTOR", "KW_FEATURE", "KW_DEF_CTX", 
                      "KW_DEF_API", "KW_SCENARIO", "KW_GIVEN", "KW_WHEN", 
                      "KW_THEN", "KW_ERROR", "ID", "STRING", "WS", "SL_COMMENT" ]

    RULE_program = 0
    RULE_definition = 1
    RULE_var_def = 2
    RULE_endpoint_def = 3
    RULE_method = 4
    RULE_actor_def = 5
    RULE_feature_def = 6
    RULE_scenario_def = 7
    RULE_given_clause = 8
    RULE_when_clause = 9
    RULE_then_clause = 10
    RULE_error_clause = 11

    ruleNames =  [ "program", "definition", "var_def", "endpoint_def", "method", 
                   "actor_def", "feature_def", "scenario_def", "given_clause", 
                   "when_clause", "then_clause", "error_clause" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    KW_ACTOR=9
    KW_FEATURE=10
    KW_DEF_CTX=11
    KW_DEF_API=12
    KW_SCENARIO=13
    KW_GIVEN=14
    KW_WHEN=15
    KW_THEN=16
    KW_ERROR=17
    ID=18
    STRING=19
    WS=20
    SL_COMMENT=21

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
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.definition()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                    break

            self.state = 29
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


        def var_def(self):
            return self.getTypedRuleContext(ReqSpecLParser.Var_defContext,0)


        def endpoint_def(self):
            return self.getTypedRuleContext(ReqSpecLParser.Endpoint_defContext,0)


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
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.actor_def()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.var_def()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.endpoint_def()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 34
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


    class Var_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_DEF_CTX(self):
            return self.getToken(ReqSpecLParser.KW_DEF_CTX, 0)

        def ID(self):
            return self.getToken(ReqSpecLParser.ID, 0)

        def STRING(self):
            return self.getToken(ReqSpecLParser.STRING, 0)

        def getRuleIndex(self):
            return ReqSpecLParser.RULE_var_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_def" ):
                listener.enterVar_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_def" ):
                listener.exitVar_def(self)




    def var_def(self):

        localctx = ReqSpecLParser.Var_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(ReqSpecLParser.KW_DEF_CTX)
            self.state = 38
            self.match(ReqSpecLParser.ID)
            self.state = 39
            self.match(ReqSpecLParser.T__0)
            self.state = 40
            self.match(ReqSpecLParser.STRING)
            self.state = 41
            self.match(ReqSpecLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Endpoint_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_DEF_API(self):
            return self.getToken(ReqSpecLParser.KW_DEF_API, 0)

        def ID(self):
            return self.getToken(ReqSpecLParser.ID, 0)

        def method(self):
            return self.getTypedRuleContext(ReqSpecLParser.MethodContext,0)


        def STRING(self):
            return self.getToken(ReqSpecLParser.STRING, 0)

        def getRuleIndex(self):
            return ReqSpecLParser.RULE_endpoint_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndpoint_def" ):
                listener.enterEndpoint_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndpoint_def" ):
                listener.exitEndpoint_def(self)




    def endpoint_def(self):

        localctx = ReqSpecLParser.Endpoint_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_endpoint_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(ReqSpecLParser.KW_DEF_API)
            self.state = 44
            self.match(ReqSpecLParser.ID)
            self.state = 45
            self.method()
            self.state = 46
            self.match(ReqSpecLParser.STRING)
            self.state = 47
            self.match(ReqSpecLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ReqSpecLParser.RULE_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod" ):
                listener.enterMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod" ):
                listener.exitMethod(self)




    def method(self):

        localctx = ReqSpecLParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
        self.enterRule(localctx, 10, self.RULE_actor_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(ReqSpecLParser.KW_ACTOR)
            self.state = 52
            self.match(ReqSpecLParser.ID)
            self.state = 53
            self.match(ReqSpecLParser.T__1)
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
        self.enterRule(localctx, 12, self.RULE_feature_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(ReqSpecLParser.KW_FEATURE)
            self.state = 56
            self.match(ReqSpecLParser.ID)
            self.state = 57
            self.match(ReqSpecLParser.T__6)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 58
                self.scenario_def()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(ReqSpecLParser.T__7)
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


        def error_clause(self):
            return self.getTypedRuleContext(ReqSpecLParser.Error_clauseContext,0)


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
        self.enterRule(localctx, 14, self.RULE_scenario_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ReqSpecLParser.KW_SCENARIO)
            self.state = 67
            self.match(ReqSpecLParser.STRING)
            self.state = 68
            self.match(ReqSpecLParser.T__6)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 69
                self.given_clause()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self.when_clause()
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 76
                self.then_clause()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 82
                self.error_clause()


            self.state = 85
            self.match(ReqSpecLParser.T__7)
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

        def ID(self):
            return self.getToken(ReqSpecLParser.ID, 0)

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
        self.enterRule(localctx, 16, self.RULE_given_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(ReqSpecLParser.KW_GIVEN)
            self.state = 88
            _la = self._input.LA(1)
            if not(_la==18 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 89
            self.match(ReqSpecLParser.T__1)
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
        self.enterRule(localctx, 18, self.RULE_when_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(ReqSpecLParser.KW_WHEN)
            self.state = 92
            self.match(ReqSpecLParser.STRING)
            self.state = 93
            self.match(ReqSpecLParser.T__1)
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
        self.enterRule(localctx, 20, self.RULE_then_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(ReqSpecLParser.KW_THEN)
            self.state = 96
            self.match(ReqSpecLParser.STRING)
            self.state = 97
            self.match(ReqSpecLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Error_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ERROR(self):
            return self.getToken(ReqSpecLParser.KW_ERROR, 0)

        def STRING(self):
            return self.getToken(ReqSpecLParser.STRING, 0)

        def getRuleIndex(self):
            return ReqSpecLParser.RULE_error_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterError_clause" ):
                listener.enterError_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitError_clause" ):
                listener.exitError_clause(self)




    def error_clause(self):

        localctx = ReqSpecLParser.Error_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_error_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(ReqSpecLParser.KW_ERROR)
            self.state = 100
            self.match(ReqSpecLParser.STRING)
            self.state = 101
            self.match(ReqSpecLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





