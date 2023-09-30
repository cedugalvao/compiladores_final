<template>
  <div class="tw-bg-gray-300 tw-h-screen">
    <div class="tw-flex tw-items-center tw-justify-center">
      <div class="tw-w-96 tw-mt-10">
        <h1 class="tw-font-bold tw-font-mono tw-text-center tw-text-xl">
          Interpretador
        </h1>
        <div class="tw-bg-white tw-m-6 tw-shadow-2xl tw-p-6 tw-rounded-md tw-space-y-2">
          <div>
            <input v-model="code" type="text" class="tw-w-full tw-bg-gray-50 tw-border tw-border-gray-300 tw-p-1" />
          </div>
          <button @click="interpret(code)"
            class="tw-w-full tw-py-2 tw-rounded-md tw-bg-blue-600 tw-text-white tw-hover:bg-blue-800">
            Interpretar
          </button>
        </div>
      </div>
    </div>
    <div class="tw-flex tw-justify-center tw-items-center">
      <div class="tw-flex">
        <div class="tw-bg-white tw-m-6 tw-shadow-2xl tw-p-6 tw-rounded-md tw-space-y-2 tw-w-1/2">
          <div class="tw-font-bold tw-font-mono tw-text-center tw-text-xl">
            Lexer
          </div>
          <div class="tw-bg-gray-50 tw-border tw-border-gray-300 tw-h-40">
            {{
              resposta
            }}</div>
        </div>
        <div class="tw-bg-white tw-m-6 tw-shadow-2xl tw-p-6 tw-rounded-md tw-space-y-2">
          <div class="tw-font-bold tw-font-mono tw-text-center tw-text-xl">
            Parser
          </div>
          <div class="tw-bg-gray-50 tw-border tw-border-gray-300 tw-h-40"></div>
        </div>
      </div>
    </div>
  </div>
  <NuxtPage />
</template>

<script>
export default {
  name: "App",
  data: () => ({
    code: "",
    resposta: ""
  }),
  methods: {
    extractLink(code) {
      const regex = /(https?:\/\/[^\s]+)/g;
      const match = code.match(regex);
      if (match) {
        return match[0];
      } else {
        return "";
      }
    },
    interpret(code) {
      // Enviar o código como JSON para o servidor Flask
      fetch('http://localhost:5000/analyze', {  // Certifique-se de que a URL corresponda ao seu servidor Flask
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code }),
      })
        .then(response => response.json())
        .then(data => {
          // Atualizar a resposta com a resposta do servidor
          this.resposta = data.message;
        })
        .catch(error => {
          console.error('Erro ao analisar código:', error);
        });
    },
  },
};
</script>
