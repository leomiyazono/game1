# -*- coding: utf-8 -*-
import streamlit as st

# Aumentar tamanho da fonte (~30%)
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-size: 130%;
    }
    </style>
""", unsafe_allow_html=True)

# Inicialização de estado
if "pontuacao" not in st.session_state:
    st.session_state.pontuacao = 0

if "respondidas" not in st.session_state:
    st.session_state.respondidas = []

perguntas = [
    {
        "pergunta": "Qual combinação abaixo representa maior risco cardiovascular?",
        "opcoes": [
            {"texto": "Hipertensão + colesterol LDL elevado", "imagem": "https://cdn-icons-png.flaticon.com/512/2966/2966489.png", "correta": True},
            {"texto": "Pressão normal + atividade física regular", "imagem": "https://cdn-icons-png.flaticon.com/512/2936/2936886.png", "correta": False},
            {"texto": "Boa hidratação + sono adequado", "imagem": "https://cdn-icons-png.flaticon.com/512/1048/1048947.png", "correta": False},
        ],
        "mensagem": "A associação de fatores de risco potencializa eventos cardiovasculares."
    },
    {
        "pergunta": "Qual tipo de colesterol está mais associado à formação de placas nas artérias?",
        "opcoes": [
            {"texto": "LDL", "imagem": "https://cdn-icons-png.flaticon.com/512/2966/2966490.png", "correta": True},
            {"texto": "HDL", "imagem": "https://cdn-icons-png.flaticon.com/512/992/992651.png", "correta": False},
            {"texto": "Triglicerídeos isolados", "imagem": "https://cdn-icons-png.flaticon.com/512/1046/1046780.png", "correta": False},
        ],
        "mensagem": "O LDL é conhecido como 'colesterol ruim'."
    },
    {
        "pergunta": "Durante um infarto, o que ocorre com o músculo cardíaco?",
        "opcoes": [
            {"texto": "Falta de oxigenação por obstrução arterial", "imagem": "https://cdn-icons-png.flaticon.com/512/2966/2966488.png", "correta": True},
            {"texto": "Excesso de oxigênio no tecido", "imagem": "https://cdn-icons-png.flaticon.com/512/728/728093.png", "correta": False},
            {"texto": "Aumento da digestão celular", "imagem": "https://cdn-icons-png.flaticon.com/512/135/135620.png", "correta": False},
        ],
        "mensagem": "O infarto ocorre por interrupção do fluxo sanguíneo."
    },
    {
        "pergunta": "Qual fator abaixo está mais relacionado à aterosclerose?",
        "opcoes": [
            {"texto": "Acúmulo de lipídios nas artérias", "imagem": "https://cdn-icons-png.flaticon.com/512/2966/2966491.png", "correta": True},
            {"texto": "Consumo elevado de água", "imagem": "https://cdn-icons-png.flaticon.com/512/728/728093.png", "correta": False},
            {"texto": "Alta ingestão de fibras", "imagem": "https://cdn-icons-png.flaticon.com/512/1046/1046751.png", "correta": False},
        ],
        "mensagem": "A aterosclerose envolve depósito de gordura nas artérias."
    },
    {
        "pergunta": "Qual parâmetro é mais utilizado para avaliar obesidade e risco cardiovascular?",
        "opcoes": [
            {"texto": "Índice de Massa Corporal (IMC)", "imagem": "https://cdn-icons-png.flaticon.com/512/3774/3774299.png", "correta": True},
            {"texto": "Altura isolada", "imagem": "https://cdn-icons-png.flaticon.com/512/2920/2920218.png", "correta": False},
            {"texto": "Cor dos olhos", "imagem": "https://cdn-icons-png.flaticon.com/512/2921/2921826.png", "correta": False},
        ],
        "mensagem": "O IMC é amplamente usado na avaliação inicial de risco."
    },
    {
        "pergunta": "Qual desses hábitos contribui diretamente para a redução da pressão arterial?",
        "opcoes": [
            {"texto": "Redução do consumo de sal", "imagem": "https://cdn-icons-png.flaticon.com/512/1046/1046784.png", "correta": True},
            {"texto": "Aumento de bebidas açucaradas", "imagem": "https://cdn-icons-png.flaticon.com/512/2405/2405479.png", "correta": False},
            {"texto": "Sedentarismo", "imagem": "https://cdn-icons-png.flaticon.com/512/2920/2920218.png", "correta": False},
        ],
        "mensagem": "O sódio influencia diretamente a pressão arterial."
    },
    {
        "pergunta": "O que melhor define um fator de risco não modificável?",
        "opcoes": [
            {"texto": "Idade", "imagem": "https://cdn-icons-png.flaticon.com/512/2922/2922510.png", "correta": True},
            {"texto": "Alimentação", "imagem": "https://cdn-icons-png.flaticon.com/512/1046/1046751.png", "correta": False},
            {"texto": "Nível de atividade física", "imagem": "https://cdn-icons-png.flaticon.com/512/2936/2936886.png", "correta": False},
        ],
        "mensagem": "Fatores não modificáveis não podem ser alterados pelo estilo de vida."
    },
    {
        "pergunta": "Qual exame mede diretamente a atividade elétrica do coração?",
        "opcoes": [
            {"texto": "Eletrocardiograma", "imagem": "https://cdn-icons-png.flaticon.com/512/2966/2966491.png", "correta": True},
            {"texto": "Ultrassom abdominal", "imagem": "https://cdn-icons-png.flaticon.com/512/2966/2966433.png", "correta": False},
            {"texto": "Hemograma", "imagem": "https://cdn-icons-png.flaticon.com/512/2966/2966445.png", "correta": False},
        ],
        "mensagem": "O ECG avalia a atividade elétrica cardíaca."
    },
    {
        "pergunta": "Qual condição está mais associada ao aumento do risco de infarto?",
        "opcoes": [
            {"texto": "Diabetes mellitus", "imagem": "https://cdn-icons-png.flaticon.com/512/2966/2966327.png", "correta": True},
            {"texto": "Boa qualidade do sono", "imagem": "https://cdn-icons-png.flaticon.com/512/1048/1048947.png", "correta": False},
            {"texto": "Hidratação adequada", "imagem": "https://cdn-icons-png.flaticon.com/512/728/728093.png", "correta": False},
        ],
        "mensagem": "O diabetes acelera processos ateroscleróticos."
    },
    {
        "pergunta": "Qual mecanismo explica o benefício do exercício físico para o coração?",
        "opcoes": [
            {"texto": "Melhora da circulação e redução da pressão arterial", "imagem": "https://cdn-icons-png.flaticon.com/512/2936/2936886.png", "correta": True},
            {"texto": "Aumento do acúmulo de gordura arterial", "imagem": "https://cdn-icons-png.flaticon.com/512/1046/1046780.png", "correta": False},
            {"texto": "Redução da frequência respiratória permanente", "imagem": "https://cdn-icons-png.flaticon.com/512/833/833472.png", "correta": False},
        ],
        "mensagem": "O exercício melhora múltiplos fatores cardiovasculares."
    }
]

st.title("🫀 Jogo Educativo: Saúde Cardiovascular")

for idx, pergunta in enumerate(perguntas):
    st.subheader(f"Pergunta {idx + 1}")
    st.write(pergunta["pergunta"])

    col1, col2, col3 = st.columns(3)
    op = pergunta["opcoes"]

    def verificar(opcao, idx):
        if idx not in st.session_state.respondidas:
            if opcao["correta"]:
                st.success("✅ Acertou!")
                st.session_state.pontuacao += 1
            else:
                st.error("❌ Errou!")
            st.info(pergunta["mensagem"])
            st.session_state.respondidas.append(idx)

    if col1.button(op[0]["texto"], key=f"{idx}_0"):
        verificar(op[0], idx)
    col1.image(op[0]["imagem"], width=120)

    if col2.button(op[1]["texto"], key=f"{idx}_1"):
        verificar(op[1], idx)
    col2.image(op[1]["imagem"], width=120)

    if col3.button(op[2]["texto"], key=f"{idx}_2"):
        verificar(op[2], idx)
    col3.image(op[2]["imagem"], width=120)

# Resultado final
if len(st.session_state.respondidas) == len(perguntas):
    st.markdown("---")
    st.header("🏁 Resultado Final")
    st.subheader(f"Pontuação: {st.session_state.pontuacao} / 10")

    if st.session_state.pontuacao >= 8:
        st.success("Excelente! Você tem ótimos conhecimentos sobre saúde cardiovascular 🫀")
    elif st.session_state.pontuacao >= 5:
        st.warning("Bom trabalho! Mas ainda há espaço para aprender mais 😉")
    else:
        st.error("Vamos melhorar! Cuidar do coração é essencial ❤️")

    st.info("Mensagem educativa: Manter alimentação equilibrada, praticar exercícios e controlar fatores de risco são fundamentais para prevenir doenças cardiovasculares.")
