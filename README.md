# Treinamento de classificador multi-classes
_(Multi-class classifier training)_

Repositório com scripts para um classificador com multi-classes.  
_Scripted repository for a multi-class classifier._


## Configurações
_(Setup)_

Python versão 3.7.1  
_Python version 3.7.1_

### Instalar dependências
_(Install dependencies)_

Clone o repositório git e instale os requerimentos:  
_Clone the git repository and install the requirements:_

```
git clone https://github.com/Lisliane/multiclass_classification
cd multiclass_classification
virtualenv -p python3 env
source env/bin/activate
pip install -r requeriments.txt
```

### Data set
_(Data set)_

Acrescente os arquivos na pasta:  
_Add the files in the folder:_

```
multiclass/dataset
```

**Dica:**  
_(Tip:)_

Caso não sejam .CSV, mude o valor da variável EXTENSION_DATASET em:  
*If they are not .CSV, change the value of the EXTENSION_DATASET variable to:*

```
multiclass/utils/settings.py
```

## Como utilizar
_(How to use)_

Para executar:  
_To execute:_

```
cd multiclass/
./main.py --option=1 --lang=PTB
```

Onde:  
_Where:_

--option: 1-Trata dados   2-Treina    3-Prediz  
_--option: 1-Treats datas   2-Train    3-Predicts_

--lang: Define idioma. Opções: PTB (português)  ENG (inglês)  
_--lang: Defines language. Options: PTB (portuguese)  ENG (english)_


Para alterar as constantes, edite o arquivo:  
_To change the constants, edit the file:_

```
multiclass/utils/settings.py
```


## Estrutura das pastas
_(Folders structure)_

As pastas foram organizadas da seguinte forma:  
_The folders were organized as follows:_

* multiclass: pasta principal da solução, contendo o arquivo main.py, que executa.  
*multiclass: main folder of the solution, containing the main.py file, which is executed.*

* multiclass/dataset: onde os dados históricos devem ser colocados.  
*multiclass/dataset: where historical data should be placed.*

* multiclass/clean: classes que limpam os dados.  
*multiclass/clean: classes that clean up data.*

* multiclass/transformer: transformar os dados.  
*multiclass/transformer: transform the data.*

* multiclass/train: treinamento do modelo.  
*multiclass/train: model training.*

* multiclass/predict: predizer.  
*multiclass/predict: predizer.*

* multiclass/utils: classes comuns entre as funcionalidades.  
*multiclass/utils: common classes between features.*


## Resultado pyreverse
_(Result pyreverse)_

```
pyreverse multiclass -o project.png
```
### Classes
_(Class)_
![Alt text](classes.project.png)

### Pacotes
_(Packages)_
![Alt text](packages.project.png)


## Autora
_(Author)_

Lisliane Zanette de Oliveira (lislianezanetteoliveira@gmail.com)
