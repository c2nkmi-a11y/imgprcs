import axios from "../api/axios";


export default function ImageUploader({ onUpload }: any) {
    const handleUpload = async (e: any) => {
        const file = e.target.files[0];
        const formData = new FormData();
        formData.append('file', file);

        const res = await axios.post("/images/upload", formData);
            onUpload(res.data);

        };

        return <input type="file" onChange={handleUpload} />;

    };