import express from 'express';
import { generatePDF } from '../playwright/generatePdf.js';

const router = express.Router();

router.post('/generate', async (req, res) => {
    try {
        const {url} = req.body;
        
        if (!url){
            return res.status(400).json({
                error: 'URL is required'
            });
        }

        if (!url.startsWith('http://') && !url.startsWith('https://')) {
            return res.status(400).json({
                error: 'Invalid URL format. Must start with http:// or https://'
            });
        }

        const pdf = await generatePDF(url);

        res.setHeader('Content-Type', 'application/pdf');
        res.setHeader(
            'Content-Disposition',
            'inline; filename="cv.pdf"'
        );

        return res.send(pdf);
        
    } catch (error){
        console.error(error);

        return res.status(500).json({
            error: 'Failed to generate PDF'
        });
    }
});

export default router;