require 'gtk2'

window = Gtk::Window.new( 
    #padrçao do metodo window
    type = Gtk::Window::TOPLEVEL)

#controla a visuallização da guia de fecha
window.decorated = true

window.show
Gtk.main