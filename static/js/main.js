/**
 * EduTrack Main JS
 * Studio Chalk Theme Interactivity
 */

document.addEventListener('DOMContentLoaded', () => {
    console.log('EduTrack - Studio Chalk Theme Loaded');

    // Add ripple-like effect to buttons on click
    const buttons = document.querySelectorAll('.sc-btn');
    buttons.forEach(btn => {
        btn.addEventListener('mousedown', function() {
            this.style.transform = 'scale(0.98)';
        });
        btn.addEventListener('mouseup', function() {
            this.style.transform = 'scale(1)';
        });
        btn.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });

    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.sc-alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
            alert.style.opacity = '0';
            alert.style.transform = 'translateX(20px)';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });
});
