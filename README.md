# ProyectoFinal - Abayay, Pasquini, Vergini

<h1>Libroteca de Opiniones</h1>
<h2>Video Demo</h2>
<p><a href="https://drive.google.com/file/d/1UEE-MpZ6jUB22bHuDPdS4sa9UVcFbvRE/view">Link a Demo del Proyecto</a></p>

El sitio web tiene como objetivo que los usuarios puedan cargar reseñas que incluyan sus opiniones sobre determinados libros.

<h3> Instalaciones requeridas: </h3>
<li> Django: pip install Django==4.1.1 </li>
<li> CKEditor: pip install django-ckeditor </li>
<li> CrispyForms: pip install django-crispy-forms </li>

Branch a utilizar en Git: <b>master</b>
<p>Hay 2 tipos de usuarios. Usuarios administradores y usuarios finales. Las funcionalidades están basadas en los mismos, así como en el caso de los usuarios no logueados. A saber:</p>

http://127.0.0.1:8000/ --- > dirige a la página de inicio.

<h3> Usuarios no logueados:</h3>
Pueden:
<li>Ver reseñas en página de inicio</li>
<li>Acceder al about --- > http://127.0.0.1:8000/about/  </li>
<li> En navbar, con el dropdown "Libros", buscar un libro por título y/o apellido del autor(http://127.0.0.1:8000/libros/busquedaLibro/), ver lista de libros (http://127.0.0.1:8000/libros/listaLibros/), de autores (http://127.0.0.1:8000/libros/listaAutores/) y de editoriales (http://127.0.0.1:8000/libros/listaEditoriales/) </li>
<li>Desde navbar, con el dropdown "Categoría", ver la lista de categorías cargadas y acceder a alguna. Si la cateogoría tiene reseñas (por ej, "ficción argentina"--- > http://127.0.0.1:8000/categoria/1/ ) , ver listado de las reseñas en esa categoría. Si no hay ninguna reseña (por ej, "filosofía"--- >  http://127.0.0.1:8000/categoria/5/", va a aprecer mensaje "Todavía no hay ninguna reseña en la categoría" </li>
<li>Ver lista de todas las reseñas; por cada una, se ve fecha de publicación, título, subtítulo, autor, categoría y primera parte del texto a traves de slice (http://127.0.0.1:8000/pages/). El template está paginado; al final de la página se puede acceder a la primera, anterior, etc. pág, según corresponda </li>
<li>Buscar reseñas sobre algun libro particular, o escritas por un usuario determinado (http://127.0.0.1:8000/busquedaPost/) </li>
<li>Leer una reseña, por ejemplo, http://127.0.0.1:8000/post/11 . El usuario no logueado puede ver la cantidad de likes y los comentarios a la reseña, pero no puede dar like ni comentar.  </li>
<li>Acceder a perfiles de usuarios, por ejemplo, a través de enlace en la vista de una reseña hacia el perfil de su autor</li>
<li>Registrarse (http://127.0.0.1:8000/accounts/signup/) o loguearse (http://127.0.0.1:8000/accounts/login/)</li>

<h3>Usuarios con perfil admin:</h3>

<table>
	<th>Username</th>
	<th>Password </th>
	<tr>
		<td>admin</td>
		<td>proyecto1234</td>
	</tr>
</table>

  <li>Realiza el CRUD de libros (http://127.0.0.1:8000/libros/libroCrear/, http://127.0.0.1:8000/libros/editarLibro/1, http://127.0.0.1:8000/libros/eliminarLibro/1), de editoriales (http://127.0.0.1:8000/libros/editorialCrear/, http://127.0.0.1:8000/libros/editarEditorial/1, http://127.0.0.1:8000/libros/eliminarEditorial/1) y autores (http://127.0.0.1:8000/libros/autorCrear/, http://127.0.0.1:8000/libros/editarAutor/1, http://127.0.0.1:8000/libros/eliminarAutor/1) para que estén disponibles para reseñar</li>
  <li>Pueden realizar reseñas</li>
 
<h3> Usuarios finales:</h3>
	
<table>
	<th>Username</th>
	<th>Password </th>
	<tr>
		<td>nicole</td>
		<td>proyecto1234</td>
	</tr>
</table>
Además de todo lo que puede hacer un usuario no logueado, pueden: 
<li> Visualizar (http://127.0.0.1:8000/accounts/profile/2) y editar (http://127.0.0.1:8000/accounts/editarPerfil/) su perfil</li>
<li>Escribir nuevas reseñas de libros ya cargados (http://127.0.0.1:8000/crearPost/), y editar (http://127.0.0.1:8000/editarPost/15) y eliminar (http://127.0.0.1:8000/eliminarPost/15) solo las reseñas que escribieron </li>
<li>Enviar mensajes a otros usuarios del sitio, desde una página en la que se listan todos los usuarios y se va ingresando a la conversación con cada uno (http://127.0.0.1:8000/accounts/conversacion/nicole/)</li>
<li>Pueden dar <i>like</i> a una reseña realizada por otro usuario.
<li>Pueden comentar una reseña realizada por otro usuario.

  <h3>Responsabilidades:</h3>
 <p>Para el desarrollo del proyecto hemos realizado una primer reunión de coordinación para identificar tareas y responsables. Luego hemos ido asignando tiempo para el desarrollo y realizando otros encuentros virtuales para ir comprobando el avance y levantar dudas y bloqueos.</p>
  
  <h4>Ludmila Vergini</h4>
  <li>Realizó el desglose inicial de tareas, contribuyó en la asignacion inicial de responsabilidades y seguimiento</li>
  <li>Participó en la confección de templates en Django</li>
  <li>Implementó la app accounts y sus funcionalidades </i>
  <li>Desarrolló vistas, modelos y formularios de la app de Libros y Blog.</li>
  <li>Desarrolló e implementó la funcionalidad de likes para cada post.</li>
  <li>Desarrolló e implentó comentarios para cada post.</li>
  <li>Subió la rama inicial del proyecto a Git</li>
  <li>Trabajó en la funcionalidad de Mensajeria</li>
  <li>Bug fixing general sobre app de Libros, Blog y accounts.</li>
  
  <h4>Mariana Abayay</h4>
  <li>Contribuyó en la asignacion inicial de responsabilidades y seguimiento</li>
  <li>Participó en la confección de templates en Django</li>
  <li>Implementó la app Blog y sus funcionalidades </i>
  <li>Desarrolló vistas, modelos y formularios de la app de Blog.</li>
  <li>Bug fixing general sobre app de Libros, Blog y accounts.</li>
  
  <h4>Marcio Pasquini</h4>
  <li>Contribuyó en la asignacion inicial de responsabilidades y seguimiento</li>
  <li>Participó en la confección de templates en Django</li>
  <li>Selección de template de bootstrap y adaptacion</li>
  <li>Trabajó en la funcionalidad de Mensajería</li>
  <li>Bug fixing general en CSS</li>
  <li>Bug fixing general sobre app de Libros, Blog y accounts.</li>
  
  <h3>Pruebas de Sistema</h3>
  
  Durante la fase de desarrollo del sistema se han ido documentando pruebas de sistema sobre distintos modulos. Las mismas han sido documentadas en el archivo: Planilla_Pruebas_de_Sistema_Coderhouse.xlsx subido a ésta plataforma.
  
<h3> Funcionalidades y demo</h3>
 Se adjunta video con demo del sitio.
 La misma cubrió las siguientes funcionalidades:
  Arranque del proyecto: http://127.0.0.1:8000/
	- se muestran las opciones que se ven, una revisión sobre la estructura de la pagina y las opciones de la nav bar.
	- se visualiza el about us: http://127.0.0.1:8000/about/
- Se muestra que funciona el admin de Django: http://127.0.0.1:8000/admin
- Se loguea con usuario admin.
	- Se muestra todo lo relacionado con la carga ed libros que es lo que esta restringido solo a los admins.
		Carga de libro, se hace enfasis en imagen: http://127.0.0.1:8000/libros/libroCrear/
- Se desloguea: http://127.0.0.1:8000/accounts/logout/
- Se loguea usuario final
	- se muestra que hay cosas q no puede hacer
	- carga una reseña, haciendo enfasis en ckeditor y en los dropdowns pre rellenados: http://127.0.0.1:8000/crearPost/
	- Busca reseña: http://127.0.0.1:8000/busquedaPost/
	- la edita: http://127.0.0.1:8000/editarPost/15
	- la visualiza en el home
	- le manda un mensaje a un usuario: http://127.0.0.1:8000/accounts/conversacion/nicole/

- Se desloguea
- Se loguea con otro usuario
	- se visualiza en la home la reseña que habia creadoe l otro usuario
	- entra a sus mensajes: http://127.0.0.1:8000/accounts/conversacion/nicole/
		- mira mensajes
		- responde: http://127.0.0.1:8000/accounts/conversacion/admin/
