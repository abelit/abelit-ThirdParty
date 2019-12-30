<template>
  <v-container fluid class="pa-0">
    <v-img
      :src="require('@/assets/images/eq5d_bg1.jpg')"
      max-height="40vh"
      :aspect-ratio="16 / 9"
    >
      <v-row align="center" justify="center" style="height: 100%">
        <v-col cols="8">
          <span class="display-3 font-weight-bold" style="color: #014759"
            >Questions?</span
          >
        </v-col>
      </v-row>
    </v-img>
    <v-row class="pt-12">
      <v-col cols="12">
        <v-row align="center" justify="center">
          <v-card
            v-for="item in questionList"
            :key="item.id"
            class="ma-3 pa-6 text-center display-1"
            color="#036f90"
            outlined
            width="240"
            height="120"
            dark
            @click="saveExamType(item)"
            >{{ item.name }}</v-card
          >
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    questionList: [
      {
        id: 1,
        name: "DCE",
        content: "EQ-PVT DCE 问卷",
        description: ""
      },
      {
        id: 2,
        name: "TTO",
        content: "EQ-PVT TTO 问卷",
        description:
          "感谢您同意参加本次调查。本次采访的目的是为了改进医疗卫生系统。我们邀请包括您在内的病人帮助我们完成这项研究。这些问题是询问人们对于健康状况和疾病的不同看法。我们感兴趣的是您的看法，这里没有正确或错误的答案。您只需告诉我们您的想法。完成本项调查大约需要30分钟。我们将对您的答案和个人信息严格保密。您准备好了吗？"
      },
      {
        id: 3,
        name: "TTO Feedback",
        content: "EQ-PVT TTO Feedback 问卷",
        description: ""
      },
      {
        id: 4,
        name: "Open Ended",
        content: "EQ-PVT Open Ended 问卷",
        description: ""
      }
    ]
  }),
  methods: {
    saveExamType(value) {
      console.log(value);
      this.getQuestionNum(value.id);
      this.$store.dispatch("setExamType", value).then(() => {
        // 跳转到指定页面
        this.$router.push({ path: "/eq" });
      });
    },
    getQuestionNum(id) {
      this.$axios
        .get("/api/question/blocks", {
          params: { type: id }
        })
        .then(res => {
          console.log(res.data);
          this.$store.dispatch("setBlocks", res.data);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>
