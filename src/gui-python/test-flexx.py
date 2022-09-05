from flexx import flx
class Exemplo(flx.Widget):

  def init(self):
    flx.Button(text='Hii')
    flx.Button(text="World")

if __name__ == '__main__':
  a = flx.App(Exemplo, title='Flexx demostration')
  m = a.launch()
  flx.run()