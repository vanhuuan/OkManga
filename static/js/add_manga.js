import {getStorage, ref, uploadBytesResumable, getDownloadURL} from "https://www.gstatic.com/firebasejs/9.6.8/firebase-storage.js";
import {initializeApp} from "https://www.gstatic.com/firebasejs/9.6.8/firebase-app.js";

export var imgUrl = ''

export function uploadThumbnail(imgThumbnail) {
    const firebaseConfig = {
        apiKey: "AIzaSyDWCDkW5O2yMc1_k_NPWWYjbR9Imh31bnI",
        authDomain: "okmanga.firebaseapp.com",
        projectId: "okmanga",
        storageBucket: "okmanga.appspot.com",
        messagingSenderId: "1032293980169",
        appId: "1:1032293980169:web:79151ba718d0054dfbc0d8",
        measurementId: "G-3M9EWBZGGC"
    };

    const firebaseApp = initializeApp(firebaseConfig);

    const storage = getStorage(firebaseApp);

    const metadata = {
        contentType: 'image/jpeg'
    };

    const storageRef = ref(storage, 'images/' + getId() + ".jpeg");
    const uploadTask = uploadBytesResumable(storageRef, imgThumbnail, metadata);
// Listen for state changes, errors, and completion of the upload.
    uploadTask.on('state_changed',
        (snapshot) => {
            // Get task progress, including the number of bytes uploaded and the total number of bytes to be uploaded
            const progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
            console.log('Upload is ' + progress + '% done');
            switch (snapshot.state) {
                case 'paused':
                    console.log('Upload is paused');
                    break;
                case 'running':
                    console.log('Upload is running');
                    document.getElementById('okay').value = "";
                    break;
            }
        },
        (error) => {
            switch (error.code) {
                case 'storage/unauthorized':
                    console.log("don't have permission to storage")
                    imgUrl = "failed";
                    break;
                case 'storage/canceled':
                    console.log("upload canceled")
                    imgUrl = "failed";
                    break;
                case 'storage/unknown':
                    console.log("unknown err")
                    console.log(error);
                    imgUrl = "failed";
                    break;
            }
        },
        () => {
            getDownloadURL(uploadTask.snapshot.ref).then((downloadURL) => {
                console.log('File available at', downloadURL);
                imgUrl = downloadURL;
                var urls = document.getElementById("urls");
                urls.value = urls.value + ";"+ downloadURL
                document.getElementById('okay').value = "okay";
            });
        }
    );
}

export function getImgUrl(){
    return imgUrl;
}

function setImgUrl(url){
    imgUrl = url;
}

function getId () {
  // Math.random should be unique because of its seeding algorithm.
  // Convert it to base 36 (numbers + letters), and grab the first 9 characters
  // after the decimal.
  return '_' + Math.random().toString(36).substr(2, 9);
};