import { createStore } from "vuex";

//import modules
import Catalogs from "@/js/store/modules/catalogs";

//

export default createStore({
    modules: {
        Catalogs,
    }
})