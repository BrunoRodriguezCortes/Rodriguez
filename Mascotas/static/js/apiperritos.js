fetch('https://api.thedogapi.com/v1/breeds')
  .then(response => response.json())
  .then(data => {
    // Manipular los datos devueltos de la API
    console.log(data);
    // Actualizar el contenido HTML con los datos
    document.getElementById('resultado').innerHTML = data;
  })
  .catch(error => {
    // Manejar cualquier error de la solicitud
    console.error('Error:', error);
  });