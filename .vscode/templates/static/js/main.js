const btndeleteinsertmedal= document.qyerySelectorAll('.btn-delete_insertmedal')

if(btndeleteinsertmedal){   //si existe lo transformamos en una lista de nodos html
 const btnarray=Array.from(btndeleteinsertmedal);
 btnarray.forEach((btn) => {
   btn.addEventListener('click', (e) => {
     if(!confirm('Esta seguro de querer borrar este registro?')){
      e.preventDefault(); //cancelar el evento click
     }
  });
 });
}