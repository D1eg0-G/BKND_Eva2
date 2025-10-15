// Funciones globales para la aplicación

document.addEventListener('DOMContentLoaded', function() {
    // Inicializar tooltips si es necesario
    initializeTooltips();
    
    // Manejar mensajes flash
    handleFlashMessages();
    
    // Inicializar formularios
    initializeForms();
});

function initializeTooltips() {
    // Implementar tooltips básicos si es necesario
    const elementsWithTooltip = document.querySelectorAll('[data-tooltip]');
    
    elementsWithTooltip.forEach(element => {
        element.addEventListener('mouseenter', showTooltip);
        element.addEventListener('mouseleave', hideTooltip);
    });
}

function showTooltip(event) {
    const tooltipText = event.target.getAttribute('data-tooltip');
    if (tooltipText) {
        // Implementar lógica para mostrar tooltip
        console.log('Tooltip:', tooltipText);
    }
}

function hideTooltip() {
    // Implementar lógica para ocultar tooltip
}

function handleFlashMessages() {
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transition = 'opacity 0.5s';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });
}

function initializeForms() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            // Validación básica del formulario
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    highlightError(field);
                } else {
                    removeErrorHighlight(field);
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                showFormError('Por favor, complete todos los campos requeridos.');
            }
        });
    });
}

function highlightError(field) {
    field.style.borderColor = '#DC3545';
    field.style.boxShadow = '0 0 0 2px rgba(220,53,69,0.25)';
}

function removeErrorHighlight(field) {
    field.style.borderColor = '';
    field.style.boxShadow = '';
}

function showFormError(message) {
    // Crear y mostrar mensaje de error
    const errorDiv = document.createElement('div');
    errorDiv.className = 'alert alert-danger';
    errorDiv.textContent = message;
    
    const forms = document.querySelectorAll('form');
    if (forms.length > 0) {
        // Inserta el error antes del primer formulario
        forms[0].insertBefore(errorDiv, forms[0].firstChild);
        
        setTimeout(() => {
            errorDiv.remove();
        }, 5000);
    }
}

// ELIMINADO: La función confirmDelete fue eliminada ya que la lógica de eliminación
// ahora se maneja completamente en model_base.html.