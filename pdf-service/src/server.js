import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import pdfRoutes from './routes/pdf.js';

dotenv.config();

const app = express();

app.use(cors());
app.use(express.json({ limit: '10mb'}));

app.use('/api/pdf', pdfRoutes);

const PORT = process.env.PORT || 3001;

app.listen(PORT, () => {
    console.log(`PDF service running on port ${PORT}`);
})