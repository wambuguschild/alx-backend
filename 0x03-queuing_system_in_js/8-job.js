export default function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    jobs.forEach((data) => {
        if (typeof data !== 'object' || data === null) {
            console.error('Invalid data format. Expected an object.');
            return;
        }

        const pushNotification = queue.create('push_notification_code_3', data);
        if (!pushNotification || !pushNotification.save) {
            console.error('Failed to create push notification.');
            return;
        }

        pushNotification.save((err) => {
            if (err) {
                console.error(`Failed to create notification job: ${err}`);
            } else {
                console.log(`Notification job created: ${pushNotification.id}`);
            }
        });

        pushNotification.on('complete', () => {
            console.log(`Notification job ${pushNotification.id} completed`);
        }).on('progress', (progress) => {
            console.log(`Notification job ${pushNotification.id} ${progress}% complete`);
        }).on('failed', (err) => {
            console.log(`Notification job ${pushNotification.id} failed: ${err}`);
        });
    });
}
