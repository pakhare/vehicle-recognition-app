
new Vue({
    el: '#app',
    data: {
         
            fetchUrl: 'http://localhost:5000/',
            selectedFile: null,
            imageUrl: '',
            processedUrl: '',
            imageReceived: false,
        
    },
    methods: {
        handleFileChange(event) {
            this.selectedFile = event.target.files[0];
        },
        uploadImage() {
            if (!this.selectedFile) {
                console.error('No file selected');
                return;
            }

            let formData = new FormData();
            formData.append('image', this.selectedFile);

            fetch(this.fetchUrl + 'upload', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                this.imageUrl = this.fetchUrl + data.imageUrl;
                this.imageReceived = true;
                this.fetchProcessedImage();
            })
            .catch(error => {
                console.error('Error uploading image:', error);
            });
        },
        fetchProcessedImage() {
            fetch(this.fetchUrl + 'upload')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                this.processedUrl = this.fetchUrl + data.processedUrl;
            })
            .catch(error => {
                console.error('Error fetching processed image:', error);
            });
        }
    }
});


