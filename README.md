Instruções para execução do caso de teste:

Pré-requisitos de ambiente:

- Instalar a versão mais atualizada do Python e selecionar o PATH na hora de realizar a instalação;
- Instalar o Robot Framework com o comando: pip install robotframework;
- Instalar o Selenium com Robot Framework com o comando: pip install robotframework-seleniumlibrary;
- Instalar uma versão estável do Selenium com o comando: pip install selenium==4.9.0
- Baixar o chromedriver no link: https://chromedriver.chromium.org/downloads
- Clicar no botão Windows e buscar a palavra: "variáveis" para acessar as Propriedades do Sistema e as Variáveis de Ambiente;
- Clicar no botão "Variáveis de Ambiente" e copiar o endereço da variável "Path";
- Colar o endereço da variável "Path" no Explorador de Arquivos e colar o arquivo do chromedriver que foi baixado anteriormente;
- Instalar o Visual Studio Code no computador.

Pré-requisitos para execução do caso de teste:
- Realizar o download do código-fonte;
- Acessar o código via Visual Studio Code;
- Executar o código do arquivo ou executar realizando o debugging.

Justificativa das escolhas feitas na implementação do teste automatizado:

- Para a resolução do caso foi indicado o uso do Robot Framework/Selenium. A escolha foi ideal, pois o Selenium é uma biblioteca popular e robusta e permite simular as ações de um usuário utilizando o sistema.
- Foi utilizada a linguagem de programação Python, pois o Framework possui a linguagem como nativa, portanto achei melhor utilizá-la.
- Foram separados os dados e as constantes, pois facilita na manutenção e reaproveitamento do código.
- Há usos de funções auxiliares para acessar os dropdowns, pois facilita na manutenção do código.
- Foram utilizadas as configurações personalizadas de navegador, pois com essa função podemos evitar a presença de pop-ups, preenchimento automático, etc que podem atrapalhar a experiência na realização da automação.
- Utilizei a verificação de sucesso para garantir que o fluxo foi executado até o fim, podendo reutilizar a mesma automação para realizarmos Testes de regressão.
