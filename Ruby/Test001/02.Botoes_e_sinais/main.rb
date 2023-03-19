require 'gtk2'


=begin

    funcionamento da chamada de eventos pela interface 

    metodo   signal_connect()
    
    GTK::ELemonto da lib.signal_connect( detailed_signal = "referencia ao evento esperado ", outros parametros) do 

        função que pode ser executada apos 

=end


#  criando botão 

button = Gtk::Button.new("Novo Botão")

#  metodo signal_connect referencia a um evento 
#  e retorna uma resposta 

button.signal_connect("clicked") do 
    puts "botão clicado"

end

#  cirand nova janela 

window = Gtk::Window.new()


#  signal_connect, evento de apertar o "X" da guia da janela

window.signal_connect("delete_event") do

    puts "evento deletado"

    #  responsavel por chamar o evento destruição da apliacaçao 
    #  evento "destroy"
    #  recebe um valor booleando 

    false

end


#  evento de fechar a janela, destruit a aplicação 

window.signal_connect("destroy") do 

    puts "destruição da aplicação "

    #  main quit destroi a aplicação, fechando a janela

    Gtk.main_quit

end


#  tamanho da largura, da borda da janela para os elementos em tela

window.border_width = 20

#  não temos um border_heigth


#  adicionando o botão a janela 

window.add(button)


#  exibir tudo que a na janela

window.show_all
Gtk.main