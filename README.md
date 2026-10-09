# Spider-Man Fan Page

Site de três páginas sobre o Homem-Aranha, feito em Flask com Bootstrap 5. Nasceu como trabalho de Desenvolvimento Web: começou em HTML e CSS puros, virou Bootstrap na segunda entrega e agora roda em cima de Flask, pronto para subir numa EC2 da AWS.

Não tem banco, não tem login, não tem painel. É um site pequeno que tenta fazer pouca coisa e fazer direito.

## O que tem aqui

- **Home**: hero com a teia e o skyline desenhados em SVG, carrossel, cards de poderes com tooltip e um accordion de curiosidades.
- **Sobre**: breadcrumb, uma linha do tempo da origem do Peter Parker, cards de poderes e uma lista de personagens que abre um modal ao clicar.
- **Contato**: formulário com validação do Bootstrap, FAQ e um toast de confirmação.

Nenhuma imagem de terceiros. Tudo que é ilustração (teia, skyline, ícone da navbar) é SVG escrito à mão no próprio HTML.

## Rodando na sua máquina

Precisa de Python 3.10 ou mais novo.

```bash
git clone <url-do-repositorio>
cd spiderman-flask

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux / macOS

pip install -r requirements.txt
python app.py
```

Abra `http://localhost:5000`.

Se estiver usando o VS Code e o F5 reclamar de conexão recusada no `debugpy`, o problema é do debugger e não do Flask. Rodar `python app.py` direto no terminal resolve.

## Estrutura

```
spiderman-flask/
├── app.py                 rotas
├── requirements.txt
├── templates/
│   ├── base.html          head, navbar, footer e scripts
│   ├── index.html
│   ├── sobre.html
│   └── contato.html
└── static/
    ├── css/style.css      estilo próprio por cima do Bootstrap
    ├── js/app.js          tooltips, modal de personagem, validação do form
    └── img/aranha.png     favicon e ícone do hero (veja "Pendências")
```

## Como as peças se encaixam

**Herança de templates.** Navbar, rodapé e carregamento de CSS e JS ficam só no `base.html`. As outras páginas estendem esse arquivo e preenchem dois blocos: `content` para o miolo da página e `extra` para o que precisa ficar fora do `<main>`, como modais e toasts.

**Link ativo do menu.** Cada rota passa uma variável `active` para o template (`home`, `sobre` ou `contato`). O `base.html` compara essa variável e aplica a classe `active` e o `aria-current="page"` só no link certo. Sem JavaScript e sem repetir o menu em três arquivos.

**Arquivos estáticos.** Todo caminho passa por `url_for('static', ...)`. Isso evita quebrar as URLs quando o app roda atrás de outro prefixo ou servidor.

**Modal de personagem.** Existe um único modal em `sobre.html`. Cada item da lista guarda nome, tag e descrição em atributos `data-*`, e o `app.js` copia esses dados para dentro do modal na hora em que ele abre.

## Limitações conhecidas

- **O formulário de contato é uma simulação.** O `app.js` intercepta o envio, valida os campos e mostra o toast, mas nada vai para o servidor. Os inputs nem têm atributo `name`. Se um dia precisar receber mensagem de verdade, é preciso adicionar os `name`, criar uma rota `POST` em `app.py` e trocar o `preventDefault` por um envio real.
- **Falta o `static/img/aranha.png`.** O arquivo não está versionado. Sem ele o favicon fica padrão e o ícone circular do hero aparece quebrado. Basta colocar uma imagem com esse nome na pasta.
- **Bootstrap e fontes vêm de CDN.** Sem internet o layout perde o estilo e as fontes caem para as do sistema.

## Subindo numa EC2

O `app.py` já sobe com `host='0.0.0.0'` na porta 5000, que é o necessário para acessar pelo IP público da instância. Do lado da AWS, o Security Group precisa liberar a porta 5000 (e a 22 para o SSH).

Dois avisos para quem usa AWS Academy: o IP público muda toda vez que o laboratório é reiniciado, e o `debug=True` do `app.py` não deve ficar ligado em nada que fique exposto por muito tempo.

## Aviso

Projeto acadêmico, feito por fã. Homem-Aranha e os personagens citados pertencem à Marvel, e este site não tem nenhuma relação com ela.

---

Yago Moraes