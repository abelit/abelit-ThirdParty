<template>
  <v-container>
    <v-card class="mt-12 pa-5">
      <v-card-title class="display-2">{{ eqLangLabels[$vuetify.lang.current].T8 }}</v-card-title>
      <v-card-text>
        <v-row justify="center" class="mt-12">
          <v-col cols="12">
            <span class="display-1">
              &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;
              {{ eqLangLabels[$vuetify.lang.current].T9 }}
            </span>
          </v-col>
        </v-row>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn x-large height="72" width="200" dark class="mt-12 lime darken-4" @click="startExam">
          <v-icon>mdi-play</v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>


<script>
import { mapState } from "vuex";
export default {
  name: "EqTip",
  data: () => ({}),
  methods: {
    startExam() {
      switch (this.examType.id) {
        case 1:
          this.$router.push({ path: "/eq/dce" });
          break;
        case 2:
          this.$router.push({ path: "/eq/tto" });
          break;
        case 3:
          this.$router.push({ path: "/eq/ttofeedback" });
          break;
        case 4:
          this.$router.push({ path: "/eq/opened" });
          break;
        case 5:
          this.$router.push({ path: "/eq/nstptto" });
          break;
        default:
          alert("题库不存在，即将跳转到首页！");
          this.$router.push({ path: "/" });
      }
    }
  },
  computed: {
    examType() {
      return this.$store.state.examType;
    },
    ...mapState(["eqLangLabels"])
  }
};
</script>