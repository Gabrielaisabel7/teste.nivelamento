async function buscarOperadora() {
    const nome = document.getElementById("search").value.trim();
    const resultsDiv = document.getElementById("results");

    if (nome === "") {
        resultsDiv.innerHTML = "<p style='color:red;'>Por favor, digite o nome da operadora.</p>";
        return;
    }

    try {
        const response = await fetch(`http://127.0.0.1:5000/buscar?q=${encodeURIComponent(nome)}`);

        if (!response.ok) {
            throw new Error("Erro ao buscar a operadora.");
        }

        const dados = await response.json();

        if (dados.length === 0 || dados.mensagem === "Nenhum resultado encontrado.") {
            resultsDiv.innerHTML = "<p style='color:red;'>Operadora não encontrada.</p>";
            return;
        }

        let html = "<h3>Resultados:</h3>";
        dados.forEach(op => {
            html += `
                <div style="margin-bottom: 10px;">
                    <p><strong>Razão Social:</strong> ${op.Razao_Social}</p>
                    <p><strong>Cidade:</strong> ${op.Cidade}</p>
                    <p><strong>UF:</strong> ${op.UF}</p>
                </div>
                <hr/>
            `;
        });

        resultsDiv.innerHTML = html;

    } catch (error) {
        resultsDiv.innerHTML = `<p style='color:red;'>Erro: ${error.message}</p>`;
    }
}
