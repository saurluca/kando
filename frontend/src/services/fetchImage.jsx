import axios from "axios";

export const fetchImage = async (prompt) => {
    const url = `https://memes.spuckteller.workers.dev/?prompt=${encodeURIComponent(prompt)}`;
    console.log("url:", url);
    const response = await axios.get(`https://memes.spuckteller.workers.dev/?prompt=${encodeURIComponent(prompt)}`, {
        responseType: "arraybuffer",
    });

    const imageBlob = new Blob([response.data], {type: 'image/png'});
    // return image url
    return URL.createObjectURL(imageBlob);
}
