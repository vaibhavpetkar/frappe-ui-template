/**
 * Frappe ERPNext Custom Theme JavaScript
 * Based on https://kymysrwf.manus.space/ design
 */

(function() {
  // Initialize when document is ready
  document.addEventListener('DOMContentLoaded', function() {
    initSidebar();
    initTopNavbar();
    initDashboard();
    initResponsiveLayout();
  });

  /**
   * Initialize sidebar functionality
   */
  function initSidebar() {
    // Toggle sidebar on mobile
    const sidebarToggle = document.querySelector('.sidebar-toggle');
    const sidebar = document.querySelector('.sidebar');
    
    if (sidebarToggle && sidebar) {
      sidebarToggle.addEventListener('click', function() {
        sidebar.classList.toggle('open');
      });
    }
    
    // Handle sidebar menu item clicks
    const menuItems = document.querySelectorAll('.sidebar-menu-item');
    menuItems.forEach(item => {
      item.addEventListener('click', function() {
        // Remove active class from all items
        menuItems.forEach(i => i.classList.remove('active'));
        // Add active class to clicked item
        this.classList.add('active');
      });
    });
  }

  /**
   * Initialize top navbar functionality
   */
  function initTopNavbar() {
    // Handle navbar item clicks
    const navItems = document.querySelectorAll('.top-navbar-item');
    navItems.forEach(item => {
      item.addEventListener('click', function() {
        // Remove active class from all items
        navItems.forEach(i => i.classList.remove('active'));
        // Add active class to clicked item
        this.classList.add('active');
      });
    });
    
    // Initialize search functionality
    const searchInput = document.querySelector('.search-bar input');
    if (searchInput) {
      searchInput.addEventListener('focus', function() {
        // Add focus class to search bar
        this.parentElement.classList.add('focused');
      });
      
      searchInput.addEventListener('blur', function() {
        // Remove focus class from search bar
        this.parentElement.classList.remove('focused');
      });
      
      // Search functionality would integrate with Frappe's search API
      searchInput.addEventListener('input', debounce(function() {
        if (this.value.length > 2) {
          // This would be replaced with actual Frappe search API call
          console.log('Searching for:', this.value);
        }
      }, 300));
    }
    
    // Initialize user menu dropdown
    const userMenu = document.querySelector('.user-menu');
    const userDropdown = document.querySelector('.user-dropdown');
    
    if (userMenu && userDropdown) {
      userMenu.addEventListener('click', function() {
        userDropdown.classList.toggle('show');
      });
      
      // Close dropdown when clicking outside
      document.addEventListener('click', function(event) {
        if (!userMenu.contains(event.target) && !userDropdown.contains(event.target)) {
          userDropdown.classList.remove('show');
        }
      });
    }
  }

  /**
   * Initialize dashboard functionality
   */
  function initDashboard() {
    // This would integrate with Frappe's dashboard API
    // For now, we'll just add some basic functionality
    
    // Handle "View all" links
    const viewAllLinks = document.querySelectorAll('.stat-card-link');
    viewAllLinks.forEach(link => {
      link.addEventListener('click', function(e) {
        e.preventDefault();
        const target = this.getAttribute('data-target');
        if (target) {
          // This would navigate to the appropriate list view in Frappe
          console.log('Navigating to:', target);
        }
      });
    });
  }

  /**
   * Initialize responsive layout
   */
  function initResponsiveLayout() {
    // Check screen size and adjust layout
    const checkScreenSize = function() {
      const sidebar = document.querySelector('.sidebar');
      const mainContent = document.querySelector('.main-content');
      
      if (window.innerWidth < 768) {
        sidebar.classList.remove('open');
        if (mainContent) {
          mainContent.style.marginLeft = '0';
        }
      } else {
        sidebar.classList.add('open');
        if (mainContent) {
          mainContent.style.marginLeft = '250px';
        }
      }
    };
    
    // Run on load and resize
    checkScreenSize();
    window.addEventListener('resize', checkScreenSize);
  }

  /**
   * Utility function to debounce function calls
   */
  function debounce(func, wait) {
    let timeout;
    return function() {
      const context = this;
      const args = arguments;
      clearTimeout(timeout);
      timeout = setTimeout(function() {
        func.apply(context, args);
      }, wait);
    };
  }
})();
