import { chromium } from 'playwright';

export async function generatePDF(url) {
    const browser = await chromium.launch({
        headless: true,
        args: ['--no-sandbox']
    });

    const page = await browser.newPage({
        viewport: {
            width: 1440,
            height: 2000
        }
    });

    await page.goto(url, {
        waitUntil: 'networkidle'
    });

    await page.emulateMedia({
        media: 'print'
    });

    const pdf = await page.pdf({
        format: 'A4',
        printBackground: true,
        margin:{
            top: '12mm',
            right: '12mm',
            bottom: '12mm',
            left: '12mm'
        }
    });

    await browser.close();

    return pdf;
}