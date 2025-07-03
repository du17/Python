# 🔍 Scanner de Portas Simples

Uma aplicação web simples para escanear portas abertas em hosts/IPs, feita com Python Flask.

## 📋 Principais Dificuldades

### 1. **Timeouts e Performance**
- **Problema**: Scan muito lento ou travando
- **Solução**: Usamos threads e timeout de 1 segundo por porta

### 2. **Muitas Conexões Simultâneas**
- **Problema**: Sistema pode travar com muitas threads
- **Solução**: Limitamos a 50 threads simultâneas

### 3. **Firewall e Segurança**
- **Problema**: Alguns hosts bloqueiam scans
- **Solução**: Use apenas em redes próprias e hosts permitidos

### 4. **Portas Privilegiadas**
- **Problema**: Algumas portas precisam de permissões especiais
- **Solução**: Execute como administrador se necessário

## 🚀 Como Rodar

### Passo 1: Instalar Python
\`\`\`bash
# Verifique se tem Python instalado
python --version
# ou
python3 --version
\`\`\`

### Passo 2: Instalar Dependências
\`\`\`bash
# Instale o Flask
pip install flask
# ou
pip3 install flask
\`\`\`

### Passo 3: Executar a Aplicação
\`\`\`bash
# Execute o arquivo principal
python app.py
# ou
python3 app.py
\`\`\`

### Passo 4: Acessar no Navegador
\`\`\`
http://localhost:5000
\`\`\`

## 🎯 Como Usar

1. **Digite o Host**: Ex: `google.com` ou `192.168.1.1`
2. **Defina o Range**: Ex: porta `1` até `100`
3. **Clique em "Iniciar Scan"**
4. **Aguarde o resultado**

## ⚠️ Avisos Importantes

- **Use apenas em redes próprias**
- **Não faça scan em servidores que não são seus**
- **Alguns antivírus podem detectar como suspeito**
- **Ranges muito grandes podem demorar muito**

## 🔧 Portas Comuns para Testar

- **21**: FTP
- **22**: SSH
- **23**: Telnet
- **25**: SMTP (Email)
- **53**: DNS
- **80**: HTTP (Sites)
- **110**: POP3 (Email)
- **443**: HTTPS (Sites Seguros)

## 🐛 Problemas Comuns

### "Erro de conexão"
- Verifique se o host existe
- Teste com `google.com` primeiro

### "Muito lento"
- Use ranges menores (ex: 1-100)
- Teste em localhost primeiro

### "Nenhuma porta aberta"
- Normal! Muitos hosts têm poucas portas abertas
- Teste portas comuns: 80, 443, 22

## 📚 Para Aprender Mais

- **Sockets em Python**: Como funciona a conexão de rede
- **Threading**: Como fazer várias coisas ao mesmo tempo
- **Flask**: Como criar aplicações web simples
- **HTML/CSS**: Como fazer interfaces bonitas
