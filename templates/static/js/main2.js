const btnDelete= document.qyerySelectorAll('.btn-delete');

if(btnDelete){   //si existe lo transformamos en una lista de nodos html
 const btnArray=Array.from(btnDelete);
 btnarray.forEach((btn) => {
   btn.addEventListener('click', (e) => {
     if(!confirm('Esta seguro de querer borrar este registro?')){
      e.preventDefault(); //cancelar el evento click
     }
  });
 });
}