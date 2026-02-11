import { useState } from "react"
import ImageUploader from "../components/ImageUploader"
import MenuBar from "../components/MenuBar"
import StatsChart from "../components/StatsChart"
import { useUndoRedo } from "../hooks/useUndoRedo"

export default function Dashboard() {
    const [stats, setStats] = useState([]);
    const { state: image, saveState } = useUndoRedo(null);

    return (
        <div className="dashboard">
            <ImageUploader onUpload={(data: any) => saveState(data.stats)} />
            {stats && <StatsChart stats={stats} />}
            </div>
    );
}
