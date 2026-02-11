export default function ImageEditor({ image }: any) {
    return image ? <img src={image} width={500} /> : <div className="p-4 text-gray-500">No image uploaded</div>;    
 }