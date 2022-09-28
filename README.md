# ProyectoFinal - Abayay, Pasquini, Vergini

<h1>Libroteca de Opiniones</h1>

El sitio web tiene como objetivo que los usuarios puedan cargar reseñas que incluyan sus opiniones sobre determinados libros.

Branch a utilizar en Git: <b>master</b></br>
Hay 2 tipos de usuarios. Usuarios administradores y usuarios finales. Las funcionalidades están basadas en los mismos. A saber

<h3>Usuarios con perfil admin:</h3>

<table>
	<th>Username</th>
	<th>Password </th>
	<tr>
		<td>admin</td>
		<td>proyecto1234</td>
	</tr>
</table>

  <li>Realiza el CRUD de libros, editoriales y autores para que estén disponibles para reseñar</li>
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
<li>Pueden darse de alta, visualizar y editar su perfil</li>
<li>Escribir nuevas reseñas de libros ya cargados</li>
<li>Buscar reseñas sobre algun libro particular</li>
<li>Enviar mensajes a otros usuarios del sitio</li>
<li>Pueden dar <i>like</i> a una reseña realizada por otro usuario.
<li>Pueden comentar una reseña realizada por otro usuario.

<h3> Instalaciones requeridas: </h3>
<li> Django: pip install Django==4.1.1 </li>
<li> CKEditor: pip install django-ckeditor </li>
<li> CrispyForms: pip install django-crispy-forms </li>

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
