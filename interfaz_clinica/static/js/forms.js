// FUNCIÓN UNIVERSAL PARA CARGAR DATOS DE EDICIÓN (API)
async function loadEditData(objectId, modelName) {
    const apiUrl = `/api/${modelName}/${objectId}/`;
    
    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error(`Error al cargar datos: ${response.statusText}`);
        }
        
        const data = await response.json();
        const form = document.getElementById('edit-form');
        
        for (const key in data) {
            if (data.hasOwnProperty(key)) {
                const fieldId = `edit_${key}`;
                const field = form.querySelector(`#${fieldId}`);
                
                if (field) {
                    let value = data[key];
                    
                    if (typeof value === 'object' && value !== null && value.id) {
                        // CRÍTICO: Si el campo de la API es un objeto (Clave Foránea), 
                        // toma solo el 'id' para asignarlo al <select> del formulario.
                        value = value.id; 
                    } else if (field.type === 'checkbox') {
                        field.checked = value;
                        continue;
                    }
                    
                    field.value = value;
}
            }
        }
        
    } catch (error) {
        console.error('Error en loadEditData:', error);
        alert('No se pudieron cargar los datos de edición. Consulte la consola para más detalles.');
    }
}

// FUNCIÓN UNIVERSAL PARA CONFIRMAR ELIMINACIÓN (Usando el formulario POST)
function confirmDelete(event, message) {
    event.preventDefault(); // Evitar el envío inmediato del formulario

    if (confirm(message)) {
        const button = event.currentTarget;
        const form = button.closest('form');
        
        // CRÍTICO: Construir la URL final antes de enviar
        const urlPattern = button.getAttribute('data-delete-url'); // Ej: /especialidades/0/eliminar/
        const objectId = button.getAttribute('data-object-id');     // Ej: 5

        if (urlPattern && objectId) {
            // Reemplazar el 0 en el patrón de URL con el ID real
            // Esto cambia la acción del formulario a /especialidades/5/eliminar/
            form.action = urlPattern.replace('0', objectId); 
            
            // Ahora enviamos el formulario con la URL de DELETE correcta y el CSRF token incluido
            form.submit();
        } else {
            console.error("Error: Atributos de URL o ID faltantes en el botón de eliminación.");
            // Si faltan atributos, simplemente envía la acción por defecto (que probablemente falle)
            form.submit();
        }
    }
}

// Inicialización automática
document.addEventListener('DOMContentLoaded', function() {
    // 1. Configurar botones de eliminar para usar el formulario POST
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            const form = this.closest('.delete-form');
            const objectName = form.getAttribute('data-object-name');
            // La función confirmDelete intercepta el click y envía el formulario con la URL correcta
            confirmDelete(e, `¿Está seguro de que desea eliminar "${objectName}"?`);
        });
    });

    // 2. Validación de formularios (Mantener si es necesario)
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = this.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.style.borderColor = '#DC3545';
                } else {
                    field.style.borderColor = '';
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                alert('Por favor, complete todos los campos requeridos.');
            }
        });
    });
});