from .state import EOF
from .tokens import TokenEof
from .tokens_base import TOKEN_COMMAND_DOUBLE_AMPERSAND
from .tokens_base import TokenOfCommand


class TokenDoubleAmpersand(TokenOfCommand):
	def __init__(self, params, *args, **kwargs):
		super().__init__([],
						 TOKEN_COMMAND_XXX,
						 'xxx', *args, **kwargs)
		self.target_command = 'ex_xxx'


def scan_command_double_ampersand(state):
	raise NotImplementedError()
	
