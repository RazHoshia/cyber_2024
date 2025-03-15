#!/bin/sh

# Navigate to the app directory
cd /app

# Check if an Angular project already exists
if [ ! -f "angular.json" ]; then
    echo "Generating new Angular project..."
    ng new my-angular-app --defaults --directory .
fi

# Start the Angular development server
ng serve --host 0.0.0.0 --port 4200
