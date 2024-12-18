$(document).ready(function() {
    loadAlunos();
});

// Função para carregar a lista de alunos
function loadAlunos() {
    $('#alunos-list').empty();

    fetch('/api/alunos/')
        .then(response => response.json())
        .then(data => {
            data.forEach(aluno => {
                $('#alunos-list').append(`
                    <tr>
                        <td>${aluno.id}</td>
                        <td>${aluno.matricula}</td>
                        <td>${aluno.nome}</td>
                        <td>${aluno.ano_ingresso}</td>
                        <td>${aluno.materias ? aluno.materias.join(', ') : ''}</td>
                        <td>${aluno.foto ? `<img src="${aluno.foto}" alt="Foto" class="img-thumbnail" width="50">` : ''}</td>
                        <td>
                            <button class="btn btn-primary btn-sm mt-1" onclick="openEditModal(${aluno.id}, '${aluno.nome}', ${aluno.ano_ingresso})">Editar</button>
                            <button class="btn btn-danger btn-sm mt-1" onclick="deleteAluno(${aluno.id})">Excluir</button>
                        </td>
                    </tr>
                `);
            });
        });
}

// Função para cadastrar um novo aluno
$('#form-cadastrar-aluno').submit(function(event) { 
    event.preventDefault();

    const matricula = $('#matricula').val().trim();
    const nome = $('#nome').val().trim();
    const ano_ingresso = $('#ano_ingresso').val();
    const fotoInput = $('#foto')[0].files[0];

    const formData = new FormData();
    formData.append('matricula', matricula);
    formData.append('nome', nome);
    formData.append('ano_ingresso', parseInt(ano_ingresso));

    if (fotoInput) {
        formData.append('foto', fotoInput);
    }

    fetch('/api/alunos/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCSRFToken()
        }
    })
    .then(response => {
        if (response.ok) {
            alert('Aluno cadastrado com sucesso!');
            $('#modalCadastrarAluno').modal('hide');
            loadAlunos();
            $('#form-cadastrar-aluno')[0].reset();
        } else {
            alert('Erro ao cadastrar aluno.');
        }
    });
});

// Função para editar os dados do aluno
function openEditModal(id, nome, ano_ingresso) {
    const newNome = prompt('Digite o nome atualizado do aluno:', nome);

    if (newNome) {
        fetch(`/api/alunos/${id}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({ nome: newNome })
        }).then(response => {
            if (response.ok) {
                alert('Aluno atualizado com sucesso!');
                loadAlunos();
            } else {
                alert('Erro ao atualizar aluno.');
            }
        });
    }
}

// Função para excluir um aluno
function deleteAluno(id) {
    if (confirm('Deseja realmente excluir este aluno?')) {
        fetch(`/api/alunos/${id}/`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': getCSRFToken()
            }
        }).then(response => {
            if (response.ok) {
                alert('Aluno excluído com sucesso!');
                loadAlunos();
            } else {
                alert('Erro ao excluir aluno.');
            }
        });
    }
}

// Função para obter o CSRF Token do Django
function getCSRFToken() {
    return $('input[name="csrfmiddlewaretoken"]').val();
}
