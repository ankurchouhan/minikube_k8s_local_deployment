# 🚀 Minikube Kubernetes Local Deployment

This project demonstrates deploying a **Flask Frontend** and an **Express Backend** locally on **Kubernetes (Minikube)**.  
It includes screenshots of deployments, services, and successful communication between both applications.

---

## 🖼️ Screenshots

Below are screenshots confirming successful deployment and communication between the **Flask Frontend** and **Express Backend**.

---

### 1️⃣ Pods and Services  
Output of `kubectl get pods` and `kubectl get svc`, showing both **Flask frontend** and **Express backend** pods and services running successfully.

![Pods and Services](./images/Screenshot%202025-12-10%20223923.png)

---

### 2️⃣ Flask Frontend (Browser Output)  
The **Flask frontend** running in the browser, successfully communicating with the **Express backend** through Kubernetes services.

![Flask Frontend](./images/Screenshot%202025-12-10%20223944.png)

---

### 3️⃣ Kubernetes Dashboard (Pods Running)  
The **Kubernetes Dashboard** view showing both application pods in a **Running** state.

![Kubernetes Dashboard](./images/Screenshot%202025-12-10%20224016.png)

---

### 4️⃣ Commands and Deployments  
Verification of deployment and command outputs confirming successful setup and operation of all Kubernetes resources.

![Commands and Deployments](./images/Screenshot%202025-12-10%20224041.png)

---

## ✅ Summary

These screenshots verify:
- Successful deployment of both **Flask Frontend** and **Express Backend** pods  
- Proper **service exposure** and **internal communication** through Kubernetes  
- Kubernetes Dashboard showing **healthy, running pods**  
- Verified **CLI outputs** for deployments and services  

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | Flask (Python) |
| **Backend** | Express.js (Node.js) |
| **Containerization** | Docker |
| **Orchestration** | Kubernetes (Minikube) |
| **Monitoring** | Kubernetes Dashboard |

---

## 🧰 Commands Used

```bash
# Build Docker images
docker build -t flask-frontend .
docker build -t express-backend .

# Push to Docker Hub
docker push ankurchouhan/flask-frontend
docker push ankurchouhan/express-backend

# Deploy to Kubernetes
kubectl apply -f flask-deployment.yaml
kubectl apply -f express-deployment.yaml

# Check resources
kubectl get pods
kubectl get svc
