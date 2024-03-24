new Vue({
            el: '#app',
            data() {
                return {
                    fetchUrl: 'http://localhost:5000/',
                    imageUrl: '',
                    processedUrl: '',
                    imageReceived: false,
                };
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

		      fetch(this.fetchUrl+'upload', {
			method: 'POST',
			body: formData
		      })
		      .then(response => {
			if (!response.ok) {
			  throw new Error('Network response was not ok');
			}
			
			this.fetchImage();
			
		      })
		      .catch(error => {
			console.error('Error uploading image:', error);
		      });
		      
		      
            	},
            	
                fetchImage() {	
                    fetch(this.fetchUrl+'upload')
                        .then(response => {
                            // Convert response to JSON
                            return response.json();
                        })
                        .then(data => {
                            // Set imageUrl to the fetched data
                            this.imageUrl = this.fetchUrl + data.imageUrl;
                            this.processedUrl = this.fetchUrl + data.processedUrl;
                            this.imageReceived = true;
                        })
                        .catch(error => {
                            console.error('Error fetching data:', error);
                        });
                        
                }
            }
        });

