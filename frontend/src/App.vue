<template>
  <div class="p-4">
    <h1>Busca de Operadoras</h1>
    <input
      v-model="busca"
      @input="buscarOperadoras"
      placeholder="Digite o nome da operadora"
    />
    <ul>
      <li v-for="(operadora, index) in operadoras" :key="index">
        {{ operadora.nome }} - {{ operadora.codigo }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      busca: "",
      operadoras: [],
    };
  },
  methods: {
    async buscarOperadoras() {
      if (this.busca.length < 2) return;

      try {
        const response = await fetch(`http://127.0.0.1:5000/buscar?query=${this.busca}`);
        const data = await response.json();
        this.operadoras = data;
      } catch (error) {
        console.error("Erro na busca:", error);
      }
    },
  },
};
</script>

<style>
input {
  margin-bottom: 20px;
  padding: 5px;
  width: 300px;
}
</style>
