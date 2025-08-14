package com.jobportal.service;

import com.jobportal.model.Application;
import com.jobportal.repository.ApplicationRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class ApplicationService {

    @Autowired
    private ApplicationRepository applicationRepository;

    public List<Application> getAllApplications() {
        return applicationRepository.findAll();
    }

    public Optional<Application> getApplicationById(Long id) {
        return applicationRepository.findById(id);
    }

    public Application saveApplication(Application application) {
        return applicationRepository.save(application);
    }

    public void deleteApplication(Long id) {
        applicationRepository.deleteById(id);
    }

    public List<Application> getApplicationsByUserId(Long userId) {
        return applicationRepository.findByUserId(userId);
    }

    public List<Application> getApplicationsByJobId(Long jobId) {
        return applicationRepository.findByJobId(jobId);
    }
}
