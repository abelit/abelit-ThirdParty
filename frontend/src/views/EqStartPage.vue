<template>
  <v-container fluid class="pa-0">
    <v-img :src="require('@/assets/images/eq5d_bg.jpg')" height="100vh">
      <v-row align="center" justify="center" style="height: 100%">
        <v-col cols="12" class="text-center">
          <v-row>
            <v-col class="mb-12" style="color: white">
              <span class="display-1">{{ examType.content }}</span>
              <v-spacer class="pb-2"></v-spacer>
              <span class="display-1" dark>
                {{
                new Date().toLocaleString()
                }}
              </span>
            </v-col>
          </v-row>
          <v-btn color="#0094ff" x-large height="72" dark class="mt-12" @click="startExam()">
            <span class="display-1">开始调查</span>
          </v-btn>
        </v-col>
      </v-row>
    </v-img>
    <!-- <eq-user-info :interviewers="interviewers" :blockQuestions="blockQuestions" v-else></eq-user-info> -->
  </v-container>
</template>

<script>
import { mapState } from "vuex";
// import EqUserInfo from "@/views/EqUserInfo";

export default {
  name: "EqStartPage",
  data: () => ({}),
  components: {
    // EqUserInfo
  },
  methods: {
    startExam() {
      this.$store.dispatch("setExamStart", true).then(() => {
        this.$router.push({ path: "/eq/user" });
      });
    }
  },
  computed: {
    ...mapState(["examType", "examStart"])
  },
  mounted() {
    console.log(this.examType);
  }
};
</script>

<style lang="scss">
.v-content__warp {
  height: 100% !important;
}
</style>
