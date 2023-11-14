<template>
  <div>
    <div class="topline">
      <img class="startimg"
           src="https://img2.baidu.com/it/u=7569883,3102876552&fm=253&fmt=auto&app=138&f=JPEG?w=251&h=201" alt=""
           @click="start()">
      <img id="yImage" class="img"
           src="https://img2.baidu.com/it/u=998595140,2432690232&fm=253&fmt=auto&app=138&f=JPG?w=500&h=500" alt="">
            <textarea class="soutput" placeholder="你的图片的描述信息" v-model="textMsg2"></textarea>
    </div>
    <div class="topline">
      <textarea class="sinput" placeholder="描述信息" v-model="textMsg"></textarea>
      <img id="myImage" class="img2" src="../assets/pic.png" alt="">

    </div>
    <div class="topline">
      <h4>Remaining commits:{{ this.num }}</h4>
      <input class="button" type="button" value="生成" @click="submit()">
    </div>
  </div>
</template>

<script>

export default {
  name: 'HelloWorld',
  data() {
    return {
      textMsg: '',
      textMsg2: '',
      num: 4,
    }
  },
  methods: {
    getstartimg() {
      this.$axios.get('http://127.0.0.1:5000/startimg').then(res => {
        let link2;
        link2 = res.data;

        const imgElement = document.getElementById("yImage");
        imgElement.src = link2;


      })
    },
    start() {
      this.getstartimg();

    },

    submit() {

      if (this.textMsg === '' || this.textMsg === ' ' || this.textMsg.length === 0) {
        return;
      }
      if (this.num === 0) {
        return;
      }
      console.log(this.textMsg)
      this.$axios.get('http://127.0.0.1:5000/makeimg', {params: {"textMsg": this.textMsg}}).then(res => {
        let link2;
        link2 = res.data;

        const imgElement = document.getElementById("myImage");
        imgElement.src = link2;

        this.num = this.num - 1;
      })

    },

  }


}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

.topline {
  width: 100%;
  height: 200px;
  position: relative;
  float: left;
  margin-top: 30px;
}

.img {
  height: 200px;
  width: 200px;
  float: left;
  margin-left: 300px;
}

.img2 {
  height: 200px;
  width: 200px;
  float: left;
  margin-left: 50px;
  margin-top: 100px;
}

.startimg {
  height: 100px;
  width: 100px;
  float: left;
  margin-left: 200px;
}

.sinput {
  float: left;
  width: 40%;
  height: 100%;
  margin-left: 29%;
  margin-top: 100px;
  text-indent: 10px;
  border: 1%;

}
.soutput{
  margin-top: 600px;
    margin-left: 100px;
  height:100px;
}
.button {
  height: 30px;
  width: 80px;
  margin-top: 50px;
}

h4 {
  margin-top: 150px;
}
</style>
