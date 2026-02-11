import { useState } from "react"
import ImageUploader from "../components/ImageUploader"
import StatsChart from "../components/StatsChart"

export default function Dashboard() {
    const [stats, setStats] = useState([]);
    
    return (
        <div className="dashboard">
            <ImageUploader onUpload={(data: any) => setStats(data.stats)} />
            {stats && <StatsChart stats={stats} />}
            </div>
    );
}
