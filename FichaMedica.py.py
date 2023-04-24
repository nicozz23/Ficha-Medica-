import os
os.system ('cls')
seguir = True
m=0
f=0
personaatendida=0
preposo=0
tiempoconsulta=0
fichamedica=0
while seguir:
    print("Servicio de atencion de urgencia")
    print("--------------------------------")
    print("1)ingresar ficha del paciente")
    print("2)actualizar ficha medica")
    print("3)asignacion de medicamentos")
    print("4)obtencion de estadisticas")
    print("5)salir")
    opcion=int(input())
    if opcion>=1 and opcion<=5:
        if opcion==1:
            fichamedica+=1
            print("ficha medica numero",fichamedica)
            print("ingrese fecha de atencion:")
            fecha=input()
            print("ingrese hora de ingreso:")
            hora=input()
            print("nombre del personal que lo atendio:")
            personal=input()
            print("")
            print("------------------------------------")
            print("")
            print("datos paciente")
            print("")
            print("--------------------------------------")
            print("nombre paciente:")
            nombre=input()
            print("apellido paciente:")
            apellido=input()
            print("rut paciente:")
            rut=input()
            print("estado civil paciente:")
            estado=input()
            print("domicilio")
            domicilio=input()
            print("telefono paciente:")
            telefono=int(input())
            print("nivel de urgencia:")
            urgencia=input()
            print("sexo paciente")
            print("1)masculino")
            print("2)femenino")
            sexo=int(input())
            if sexo==1:
                m+=1
            elif sexo==2:
                f+=1
            print("ingrese edad:")
            edad=int(input())
            if edad>=1 and edad<=120:
                print("edad valida")
            else:
                print("ingrese edad valida")
               
            print("grupo sanguineo paciente")
            sangre=input()
            print("asiste acompañado:")
            compañia=input()
            print("")    
            print("-----------------------------------------------------------")    
            print("Servicio de atencion de urgencia")
            print("-----------------------------------------------------------") 
            personaatendida+=1
            #OPCION 2 "FICHA PACIENTE"
            print("FICHA PACIENTE: ")
            print("")
            print("fecha de atencion:",fecha)
            print("hora de atencion:",hora)
            print("personal que lo atendio:",personal)
            print("nombre paciente:",nombre)
            print("apellido paciente:",apellido)
            print("rut paciente:",rut)
            print("estado civil:",estado)
            print("domicilio:",domicilio)
            print("telefono:",telefono)
            print("nivel urgencia:",urgencia)
            print("sexo:",sexo)
            print("edad:",edad)
            print("grupo sanguineo:",sangre)
            print("asiste acompañado:",compañia)
            print("")    
            print("-----------------------------------------------------------")    
            print("Servicio de atencion de urgencia")
            print("-----------------------------------------------------------") 
            print("INFORMACION DE ATENCION")
            print("Motivo de consulta medica: ")
            motivo=input()
            print("ingrese nombre medico: ")
            nombremedico=input()
            print("ingrese especialidad de medico: ")
            especialidad=input()
            print("ingrese sintomas paciente:" )
            sintomas=input()
            print("ingrese diagnostico: ")
            diagnostico=input()
            print("Reposo para paciente")
            print("1)si")
            print("2)no")
            reposo=int(input())
            if reposo==1:
                preposo+=1
                print("Cantidad de dias de reposo: ")
                dias=int(input())   
                print("")    
                print("-----------------------------------------------------------")    
                print("Servicio de atencion de urgencia")
                print("-----------------------------------------------------------") 
                print("Motivo de consula medica: ",motivo)
                print("Nombre de medico: ",nombremedico)
                print("Especialidad Medico: ",especialidad)
                print("Sintomas de paciente: ",sintomas)   
                print("Diagnostico a tratar: ",diagnostico)
                print("Necesita ",dias," de reposo ")
                
            else:
                print("Motivo de consula medica: ",motivo)
                print("Nombre de medico: ",nombremedico)
                print("Especialidad Medico: ",especialidad)
                print("Sintomas de paciente: ",sintomas)   
                print("Diagnostico a tratar: ",diagnostico)
                print("Paciente no necesita reposo") 
                print("")    
                print("-----------------------------------------------------------")    
                print("Servicio de atencion de urgencia")
                print("-----------------------------------------------------------") 
            print("tiempo consulta (en minutos)")
            tiempoconsulta=int(input())
            tiempoconsulta+=tiempoconsulta
        
            #OPCION 3 "MEDICAMENTOS:"
            print("ASIGNACION DE MEDICAMENTOS")
            print("-------------------------------------------------------------------")
            print("Ingrese cantidad de medicamentos: ")
            medicamentos=int(input())
            print("")
            print("Medicamentos: ")
            print("1)Paracetamol")
            print("2)Lidocaína")
            print("3) Omeprazol")
            print("4) Penicilina")
            print("5) Salbutamol")
            print("Seleccione medicamento")
            medicamento_2=int(input())
            if medicamento_2==1:
                print("Ha seleccionado: ",medicamentos,"paracetamol(es)")
            elif medicamento_2==2:    
                print("Ha seleccionado: ",medicamentos,"Lidocaina(s)")
            elif medicamento_2==3:
                print("Ha seleccionado: ",medicamentos,"omeprazol(es)")
            elif medicamento_2==4:
                print("Ha seleccionado: ",medicamentos,"penicilina(s)")     
            elif medicamento_2==5:
                print("Ha seleccionado: ",medicamentos,"Salbutamol(es))")           
            else:
                print("Seleccione opcion valida")    
        elif opcion==2:
            print("Debe Seleccionar opcion 1 antes de comenzar con la opcion 2")
        elif opcion==3:
            print("Debe Seleccionar opcion 1 antes de comenzar con la opcion 3")
        elif opcion==4:
            print("cantidad de personas atendidas",personaatendida)
            print("cantidad de hombres atendidos",m)
            print("cantidad de mujeres atendidas",f)
            print("personas que necesitan reposo",preposo)
            print("tiempo de atencion total",tiempoconsulta)
            print("promedio de atencion en minutos",tiempoconsulta/personaatendida)
        elif opcion==5:
            seguir=False
            print("cerrando sistema...")



    else:
        print("ingrese un numero valido")        
