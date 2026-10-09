// Ativa todos os tooltips da página
document.addEventListener('DOMContentLoaded', function () {
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    tooltipTriggerList.forEach(el => new bootstrap.Tooltip(el));

    // Preenche o modal de personagem (sobre.html) com os dados do botão clicado
    const personagemModal = document.getElementById('personagemModal');
    if (personagemModal) {
        personagemModal.addEventListener('show.bs.modal', function (event) {
            const button = event.relatedTarget;
            const nome = button.getAttribute('data-nome');
            const tag = button.getAttribute('data-tag');
            const desc = button.getAttribute('data-desc');
            personagemModal.querySelector('#personagemModalLabel').textContent = nome;
            personagemModal.querySelector('#personagemModalDesc').textContent = desc;
            const tagEl = personagemModal.querySelector('#personagemModalTag');
            if (tagEl) tagEl.textContent = tag || '';
        });
    }

    // Validação do formulário (contato.html) + toast de confirmação
    const form = document.getElementById('formContato');
    if (form) {
        form.addEventListener('submit', function (event) {
            event.preventDefault();
            event.stopPropagation();

            if (!form.checkValidity()) {
                form.classList.add('was-validated');
                return;
            }

            form.classList.add('was-validated');
            const toastEl = document.getElementById('toastEnvio');
            const toast = new bootstrap.Toast(toastEl);
            toast.show();

            form.reset();
            form.classList.remove('was-validated');
        });
    }
});
