$(document).ready( function () {
    $('#tabla_empleados').DataTable({
        "autoWidth": false,
        "oLanguage": {
            "sLengthMenu": "Mostrando _MENU_ registros por p&aacute;gina",
            "sZeroRecords": "...",
            "sInfo": "Mostrando _START_ a _END_ de _TOTAL_ registros",
            // "sInfoEmpty": "Mostrando 0 a 0 de 0 registros",
            "sSearch": "Buscar:",
            "sProcessing": "Cargando datos...",
            "oPaginate": {
                "sFirst": "Primero",
                "sPrevious": "Anterior",
                "sNext": "Siguiente",
                "sLast": "\xdaltimo"
            },
            "sInfoFiltered": "(Filtrado de un total de _MAX_ registros)"
        },
    });
} );

function abrirForm() {
    $("#form_registrar").show();
}