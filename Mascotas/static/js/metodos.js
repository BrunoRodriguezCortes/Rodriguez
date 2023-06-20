
//función que envia el contenido a un elemento de tipo textarea
function CrearCarta(){
    var genero="";
    var a=document.getElementById("rut").value;
    var b=document.getElementById("nom").value;
    var c=document.getElementById("apeP").value;
    var d=document.getElementById("apeM").value;
    var e=document.getElementById("edad").value;
    var f=parseInt(document.getElementById("genero").value);
    var n=document.getElementById("fecha").value;
    var x=document.getElementById("direccion").value;
    
    var elementoGenero = document.getElementById('genero');
    var indiceSeleccionado = elementoGenero.selectedIndex;  //seleccionamos el indice elegido
    var gen=elementoGenero.options[indiceSeleccionado].text;
    var direc = document.getElementById('direccion').text;
    
    /*
        if (f===1){
        gen='Mujer';
        }
        if (f===2){
        gen='Hombre';
        }
        if (f===3){
        gen='Otro Genero';
        }
        */

    /*
        if (x===1){
        gen='Maipú';
        }
        if (x===2){
        gen='Pudahuel';
        }
        if (x===3){
        gen='Otra comuna';
        }
        */

        var cadena= "Datos de contacto: \n" 
                +"Rut: " + a + "\n" + "Nombre: " + b + "\n"+ "Ap. Paterno: " + c 
                + "\n" + "Ap. Materno: "+ d + "\n" + "Edad: " + e 
                + "\n" + "Fecha de nacimiento: " + n
                + "\n" + "Genero: " + gen
                + "\n" + "Direccion: " + x ;  
                
        document.getElementById("carta").value=cadena;
    }




    //función que cambia el color de fondo a orange
    function colorOrange(obj){
        obj.style.backgroundColor='orange';
    }

    function colorBlanco(obj){
        obj.style.backgroundColor='black';
    }

    function upperText(texto)
    {
        const x = texto;
        x.value= x.value.toUpperCase();
    }

    function colorFondo(obj){
        obj.style.backgroundColor='orange';
    }