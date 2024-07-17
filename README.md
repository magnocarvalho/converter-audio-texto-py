# convert-audio-to-text-py

## Convert Audio Mp3 to Text Python

The script converts an MP3 file to WAV format and splits the file into 60-second tracks for upload, so as not to exceed the limit allowed by the Google Cloud Speech-to-Text API, which is 10 MB, and finally saves the result to the file.

## Detailed Steps and Requirements


### Install Dependencies:

```sh
pip install pydub google-cloud-speech
```

### Google Credentials:

Go to the Google Cloud Console.
* Navigate to "IAM & Admin" > "Service Accounts".
Find the service account you created.
* Go to the "Keys" tab and click "Add Key" > "Create new key".
Select the JSON format and download the file.

The JSON file should have a format similar to this:

```json
{
    "type": "service_account",
    "project_id": "your-project-id",
    "private_key_id": "your-private-key-id",
    "private_key": "-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY\n-----END PRIVATE KEY-----\n",
    "client_email": "your-service-account-email@your-project-id.iam.gserviceaccount.com",
    "client_id": "your-client-id",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your-service-account-email%40your-project-id.iam.gserviceaccount.com"
}
```

Update the file path in your code to point to the newly downloaded file.

### Files

* Replace "path/to/your/api_key.json" with the actual path of your Google Cloud JSON API key.
* Replace "path/to/your/audio/file.wav" with the actual path of your WAV audio file.
* Replace "path/to/your/transcription/file.txt" with the path where you want to save the transcription.

### Download and Set Up FFmpeg:

Make sure FFmpeg is installed and properly configured in the system PATH. You can test this by running ffmpeg -version in the terminal.

```sh
ffmpeg -version
```


#### Windows
* Download FFmpeg:

* Go to the FFmpeg download page.
Download the appropriate version for your operating system. 
https://ffmpeg.org/download.html

Extract the files:

* Extract the contents of the zip file to a folder, for example, C:\ffmpeg.
Add FFmpeg to the PATH:

Open "Control Panel".
Go to "System and Security" > "System" > "Advanced system settings".
* Click the "Environment Variables" button.
In the "System variables" section, find the Path variable and click "Edit".
Add the path to the FFmpeg bin folder, for example, C:\ffmpeg\bin.
Click "OK" to save the changes.

#### macOS
- Install FFmpeg using Homebrew:
- Open Terminal and run the following command:

```sh
brew install ffmpeg
```

#### Linux

- Install FFmpeg using the package manager:
- Open Terminal and run the appropriate command for your distribution:

```sh
sudo apt update
sudo apt install ffmpeg
```

# PT-BR

## Convert Audio Mp3 to Text Python

O Script convert um arquivo MP3 no formato WAV e divide o arquivo em faixas de 60 segundo para o upload, para não excede o limite permitido pela API do Google Cloud Speech-to-Text, que é de 10 MB e no final salva o resultado no arquivo

## Passos Detalhados E Requisitos


### Instalar Dependências:

```sh
pip install pydub google-cloud-speech
```

### Google Credenciais:

Vá para o Google Cloud Console.
* Navegue até "IAM & Admin" > "Service Accounts".
Encontre a conta de serviço que você criou.
* Vá para a aba "Keys" e clique em "Add Key" > "Create new key".
Selecione o formato JSON e baixe o arquivo.

O arquivo JSON deve ter um formato semelhante a este:

```json
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "your-private-key-id",
  "private_key": "-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY\n-----END PRIVATE KEY-----\n",
  "client_email": "your-service-account-email@your-project-id.iam.gserviceaccount.com",
  "client_id": "your-client-id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your-service-account-email%40your-project-id.iam.gserviceaccount.com"
}
```

Atualize o caminho do arquivo JSON no seu código para apontar para o novo arquivo baixado.

### Arquivos

* Substitua "caminho/para/sua/api_key.json" pelo caminho real da sua API key JSON do Google Cloud.
* Substitua "caminho/para/seu/arquivo.wav" pelo caminho real do seu arquivo de áudio WAV.
* Substitua "caminho/para/seu/arquivo.txt" pelo caminho onde você deseja salvar a transcrição.

### Baixar e Configurar o FFmpeg:

Certifique-se de que o FFmpeg está instalado e configurado corretamente no PATH do sistema. Você pode testar isso executando ffmpeg -version no terminal.

```sh
ffmpeg -version
```


#### Windows
* Baixe o FFmpeg:

* Vá para a página de download do FFmpeg.
Baixe a versão adequada para o seu sistema operacional. 
https://ffmpeg.org/download.html

Extraia os arquivos:

* Extraia o conteúdo do arquivo zip para uma pasta, por exemplo, C:\ffmpeg.
Adicione o FFmpeg ao PATH:

Abra o "Painel de Controle".
Vá para "Sistema e Segurança" > "Sistema" > "Configurações avançadas do sistema".
* Clique no botão "Variáveis de Ambiente".
Na seção "Variáveis do sistema", encontre a variável Path e clique em "Editar".
Adicione o caminho para a pasta bin do FFmpeg, por exemplo, C:\ffmpeg\bin.
Clique em "OK" para salvar as alterações.

#### macOS
- Instale o FFmpeg usando Homebrew:
- Abra o Terminal e execute o seguinte comando:

```sh
brew install ffmpeg
```

#### Linux

- Instale o FFmpeg usando o gerenciador de pacotes:
- Abra o Terminal e execute o comando apropriado para sua distribuição:

```sh
sudo apt update
sudo apt install ffmpeg
```

