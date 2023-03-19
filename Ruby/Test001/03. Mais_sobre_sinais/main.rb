require 'gtk2'


=begin

    **signal_connect()

        funcionamento da recebimento de eventos pela interface 

        metodo   signal_connect()
            
            GTK::ELemonto da lib.signal_connect( 
                detailed_signal = "referencia ao evento esperado ", 
                outros parametros(opcional) ) 
            do 

                    função que pode ser executada apos receber o sinal

            end

    **signal_connect_after()

        função que recebe um sinal, e so executa depois do handler padrão 

        metodo   signal_connect_after()
        
            GTK::ELemonto da lib.signal_connect( 
                detailed_signal = "referencia ao evento esperado ", 
                outros parametros(opcional) ) 
            do 

                    função que pode ser executada apos receber o sinal

            end



    **signal_emit()

        funcionamento da para emitir sinal de eventos pela interface 

        metodo   signal_emit()
        
            GTK::ELemonto da lib.signal_connect( 
                detailed_signal = "referencia ao sinal emitido ", 
                outros parametros(opcional) ) 
            do 

                    função que pode ser executada 

            end


    **signal_emit_stop()

        função para para de emitir um sinal

        metodo signal_emit_stop()

            GTK::ELemonto da lib.signal_emit_stop() 

    
=end


#  criando botões

button_l = Gtk::Button.new("listiner")
button_e = Gtk::Button.new("emitir sinal")


button_l.signal_connect("clicked") do 
   
    puts "botão clicado"

end

#  função que recebe um sinal, e so executa depois do handler padrão 

button_l.signal_connect_after("clicked") do
   
    puts "resposta apos o handler padrao "

end


button_e.signal_connect("clicked") do 
   
    #  funcionamento da para emitir sinal de eventos pela interface 

    button_l.signal_emit("clicked")

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

window.border_width = 80

#  não temos um border_heigth


#  adicionando o botoões a janela 

window.add(button_e)



#  exibir tudo que a na janela

window.show_all
Gtk.main