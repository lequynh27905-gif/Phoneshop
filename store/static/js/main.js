// Dark Mystical Theme - Advanced JavaScript

// Add to cart functionality
function addToCart(phoneId, quantity = 1) {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value || getCookie('csrftoken');
    
    const button = event.target;
    const originalText = button.textContent;
    button.textContent = '⏳ Đang thêm...';
    button.disabled = true;
    
    fetch('/cart/add/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken
        },
        body: `phone_id=${phoneId}&quantity=${quantity}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showNotification(data.message, 'success');
            updateCartBadge(data.cart_count);
        } else {
            showNotification(data.message, 'error');
        }
        button.innerHTML = originalText;
        button.disabled = false;
    })
    .catch(error => {
        console.error('Error:', error);
        showNotification('Có lỗi xảy ra', 'error');
        button.innerHTML = originalText;
        button.disabled = false;
    });
}

// Get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Update cart badge
function updateCartBadge(count) {
    const badge = document.querySelector('.cart-badge');
    if (badge) {
        badge.textContent = count;
        badge.style.animation = 'pulse 0.5s';
    }
}

// Show notification
function showNotification(message, type = 'info') {
    const container = document.querySelector('.messages') || document.body;
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.innerHTML = `
        <div class="d-flex align-center justify-between">
            <span>${message}</span>
            <button type="button" class="btn-close" onclick="this.parentElement.parentElement.remove()" style="background: none; border: none; color: inherit; cursor: pointer; font-size: 20px;">&times;</button>
        </div>
    `;
    container.insertBefore(alertDiv, container.firstChild);
    
    setTimeout(() => {
        alertDiv.style.opacity = '0';
        alertDiv.style.transition = 'opacity 0.3s ease';
        setTimeout(() => alertDiv.remove(), 300);
    }, 3000);
}

// Image preview
document.addEventListener('DOMContentLoaded', function() {
    // Initialize animations
    initAnimations();
    
    // Image preview functionality
    const imageInputs = document.querySelectorAll('input[type="file"]');
    imageInputs.forEach(input => {
        input.addEventListener('change', function(e) {
            const reader = new FileReader();
            reader.onload = function(event) {
                const preview = document.getElementById('preview-' + this.id);
                if (preview) {
                    preview.src = event.target.result;
                    preview.style.opacity = '0';
                    preview.style.transition = 'opacity 0.3s ease';
                    setTimeout(() => preview.style.opacity = '1', 10);
                }
            };
            if (this.files && this.files[0]) {
                reader.readAsDataURL(this.files[0]);
            }
        });
    });
    
    // Add hover effects to product cards
    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // Smooth scroll for anchors
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Initialize animations
function initAnimations() {
    const elements = document.querySelectorAll('[class*="fadeInUp"], [class*="slideInLeft"]');
    elements.forEach((el, index) => {
        el.style.animation = `fadeInUp ${0.6 + index * 0.1}s ease 0s forwards`;
        el.style.opacity = '0';
    });
}

// Show/Hide password
function togglePassword(inputId) {
    const input = document.getElementById(inputId);
    const button = event.target;
    if (input.type === 'password') {
        input.type = 'text';
        button.textContent = '👁️‍🗨️ Ẩn';
    } else {
        input.type = 'password';
        button.textContent = '👁️ Hiện';
    }
}

// Add to wishlist
function addToWishlist(phoneId) {
    const csrftoken = getCookie('csrftoken');
    
    fetch(`/wishlist/add/${phoneId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        }
    })
    .then(response => response.json())
    .then(data => {
        showNotification(data.message, 'success');
        const button = event.target;
        if (button.classList.contains('in-wishlist')) {
            button.classList.remove('in-wishlist');
        } else {
            button.classList.add('in-wishlist');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showNotification('Có lỗi xảy ra', 'error');
    });
}

// Parallax effect for hero section
window.addEventListener('scroll', function() {
    const hero = document.querySelector('.hero-section');
    if (hero) {
        const scrollY = window.scrollY;
        hero.style.backgroundPosition = `0 ${scrollY * 0.5}px`;
    }
});

// Fade in on scroll
function fadeInOnScroll() {
    const elements = document.querySelectorAll('.product-card');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fadeInUp 0.6s ease forwards';
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    
    elements.forEach(el => observer.observe(el));
}

// Initialize fade in on scroll when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', fadeInOnScroll);
} else {
    fadeInOnScroll();
}

// Quantity input validation
document.addEventListener('change', function(e) {
    if (e.target.classList.contains('quantity-input')) {
        const max = parseInt(e.target.getAttribute('max')) || 999;
        const min = parseInt(e.target.getAttribute('min')) || 1;
        let value = parseInt(e.target.value);
        
        if (value < min) e.target.value = min;
        if (value > max) {
            e.target.value = max;
            showNotification(`Số lượng tối đa là ${max}`, 'warning');
        }
    }
});
