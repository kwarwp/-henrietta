
{'date': 'Sat May 26 2018 16:46:00.10 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 70
  print("contagem:", responde(historia,SUJEITO, VERBO, OBJETO)
                                                                      ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Oct 02 2019 13:58:08.419 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 81
    print("TAGGER", TAGGER)
NameError: name 'TAGGER' is not defined
'''},